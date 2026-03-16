"""
Terminal Error Debugger - Gemini Live Agent Challenge
An intelligent terminal assistant powered by Gemini AI.
Features: Command execution, error analysis, command explanation, screenshot analysis
"""

import os
import subprocess
import sys
import json
from datetime import datetime
from pathlib import Path
from io import BytesIO

# Try-except for headless environments (Cloud Run)
try:
    import mss
    from PIL import Image
    HAS_SCREEN = True
except ImportError:
    HAS_SCREEN = False

import vertexai
from vertexai.generative_models import GenerativeModel, Image as VertexImage

# --- Configuration (Optimized for Cloud Run) ---
# Automatically pulls from GCP environment or defaults to your project
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT", "terminal-debugger")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")

# Initialize Vertex AI
# Note: On Cloud Run, it will use the default service account automatically.
vertexai.init(project=PROJECT_ID, location=LOCATION)

# Gemini model (Using the latest 2.0 Flash for speed)
model = GenerativeModel("gemini-2.0-flash-001")

# History file setup
HISTORY_DIR = Path.home() / ".terminal-debugger"
HISTORY_DIR.mkdir(exist_ok=True)
HISTORY_FILE = HISTORY_DIR / "history.json"
MAX_HISTORY = 100

def load_history():
    if HISTORY_FILE.exists():
        try:
            with open(HISTORY_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history[-MAX_HISTORY:], f)

def analyze_output(command, output, exit_code):
    status = "SUCCESS" if exit_code == 0 else "ERROR"
    prompt = f"""You are an expert terminal assistant. 
    Command: `{command}` | Exit Code: {exit_code} ({status})
    Output: ```{output}```
    Provide: 1. Status 2. Concise Explanation 3. EXACT fix command or follow-up.
    Format: ✅/❌ [Status] \n 📝 [Explanation] \n 💡 [Suggestion]"""
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error analyzing: {str(e)}"

def generate_command(task):
    """NL to CLI feature: Converts 'make a file' to 'touch file'."""
    prompt = f"Convert this task into a single macOS/Linux terminal command. Output ONLY the raw command, no backticks, no text: '{task}'"
    try:
        response = model.generate_content(prompt)
        return response.text.strip().replace('`', '')
    except Exception as e:
        return f"Error: {str(e)}"

def explain_command(command):
    prompt = f"Explain this command simply: `{command}`. Provide: What it does, parts breakdown, and risks."
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error explaining: {str(e)}"

def analyze_screenshot():
    if not HAS_SCREEN:
        return "❌ Error: Screenshot features are not available in this environment (Headless/Cloud)."

    print("\n📸 Capturing screen...")
    try:
        with mss.mss() as sct:
            monitor = sct.monitors[1]
            screenshot = sct.grab(monitor)
            img = Image.frombytes('RGB', screenshot.size, screenshot.bgra)
            
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            vertex_image = VertexImage.from_bytes(buffer.getvalue())

            print("🤖 Analyzing screenshot for errors...")
            prompt = "Extract visible errors from this screenshot and suggest terminal commands to fix them."
            response = model.generate_content([prompt, vertex_image])
            return response.text
    except Exception as e:
        return f"Error analyzing screenshot: {str(e)}"

def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
        output = result.stdout + (result.stderr if result.stderr else "")
        return output, result.returncode
    except Exception as e:
        return f"Error: {str(e)}", 1

def show_help():
    print("""
    🛠️  COMMANDS:
    - <command>       : Run any terminal command
    - ask <task>      : Get a command for a task (e.g. 'ask list files')
    - explain <cmd>   : Explain what a command does
    - screenshot      : Analyze screen for errors (Local only)
    - history / clear : Manage session
    - q / exit        : Quit
    """)

def interactive_mode():
    history = load_history()
    print("\n" + "="*40 + "\n🔧 SMART TERMINAL DEBUGGER (Gemini Live)\n" + "="*40)
    show_help()

    while True:
        try:
            cmd = input("\n$ ").strip()
            if not cmd: continue
            if cmd.lower() in ['q', 'quit', 'exit']: break

            # Special Handlers
            if cmd.lower() == 'help': show_help(); continue
            if cmd.lower() == 'clear': os.system('clear'); continue
            
            if cmd.lower().startswith('ask '):
                task = cmd[4:].strip()
                suggestion = generate_command(task)
                print(f"➜ Suggested Command: {suggestion}")
                continue

            if cmd.lower().startswith('explain '):
                print(explain_command(cmd[8:].strip())); continue

            if cmd.lower() == 'screenshot':
                print(analyze_screenshot()); continue

            # Standard Execution
            output, exit_code = run_command(cmd)
            print(f"\n{output}\n" + "-"*20 + "\n🤖 AI Analysis:\n" + analyze_output(cmd, output, exit_code))

        except KeyboardInterrupt: break
    save_history(history)

if __name__ == "__main__":
    # Cloud Run dynamic port binding
    port = int(os.environ.get("PORT", 8080))
    interactive_mode()
