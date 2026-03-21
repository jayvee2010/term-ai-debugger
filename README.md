<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=F97316&height=200&section=header&text=Term-AI-Debugger&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Your%20terminal%20finally%20talks%20back.&descAlignY=58&descAlign=50"/>

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Gemini_2.0_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Google Cloud Run](https://img.shields.io/badge/Cloud_Run-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![Shell](https://img.shields.io/badge/Bash-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)

[![Author](https://img.shields.io/badge/Author-jayvee2010-F97316?style=flat-square&logo=github)](https://github.com/jayvee2010)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

</div>

---

## 💡 The Problem

Every developer knows this feeling:

```bash
$ python app.py
Traceback (most recent call last):
  File "app.py", line 12, in <module>
    result = calculate(data)
NameError: name 'data' is not defined
```

You stare at it. You Google it. You waste 10 minutes on Stack Overflow for a 10-second fix.

**Most terminals are silent.** When a command fails, you get a cryptic error and no guidance. That's the problem Term-AI-Debugger solves.

---

## 🤖 The Solution

**Term-AI-Debugger** is an agentic terminal assistant that wraps your shell, watches every command you run, and uses **Gemini 2.0 Flash** to explain failures and suggest exact fixes — in real time.

```bash
$ python app.py

❌ Command failed (exit code 1)

╔══════════════════════════════════════════╗
║           🤖 AI Analysis                ║
╠══════════════════════════════════════════╣
║ 📝 Explanation:                         ║
║  The variable 'data' is used on line 12  ║
║  but was never defined. Python cannot    ║
║  find it in the current scope.           ║
║                                          ║
║ 💡 Suggestion:                          ║
║  Add before line 12:                     ║
║  data = []  # or your intended value     ║
╚══════════════════════════════════════════╝
```

---

## ✨ Features

### 🐛 Auto-Debugging
Catches and explains errors from **Python**, **Node.js**, and **Bash** the moment they happen — no copy-pasting into ChatGPT required.

### 💬 Natural Language Commands
Don't remember the exact syntax? Just describe what you want:
```bash
$ ask create a new react app
→ npx create-react-app my-app
```

### 🔎 Command Explainer
See a scary command online? Understand it before you run it:
```bash
$ explain rm -rf /tmp/old-files
→ ⚠️  This permanently deletes everything inside /tmp/old-files.
   The -r flag removes directories recursively, -f forces it with no prompts.
   Safe to run only if you're sure about the path.
```

### ☁️ Cloud-Native Brain
The AI reasoning layer runs on **Google Cloud Run** — making it fast, scalable, and always available without heavy local compute.

---

## ⚙️ How It Works

```
┌─────────────────────────────────────────────────────┐
│                   Your Terminal                      │
│                                                      │
│  $ python app.py                                     │
│         │                                            │
│         ▼                                            │
│  ┌─────────────┐    exit code ≠ 0?                  │
│  │   Wrapper   │ ──────────────────► Skip (success) │
│  │   Script    │                                     │
│  └─────────────┘                                     │
│         │ yes — failure detected                     │
│         ▼                                            │
│  Captures: command + stderr                          │
│         │                                            │
│         ▼                                            │
│  ┌──────────────────┐                               │
│  │  Google Cloud    │                               │
│  │  Run Backend     │ ◄── sends error context       │
│  └──────────────────┘                               │
│         │                                            │
│         ▼                                            │
│  ┌──────────────────┐                               │
│  │ Gemini 2.0 Flash │ — agentic reasoning           │
│  └──────────────────┘                               │
│         │                                            │
│         ▼                                            │
│  📝 Explanation + 💡 Fix printed to terminal        │
└─────────────────────────────────────────────────────┘
```

**Four steps under the hood:**

1. **Intercept** — The wrapper script captures the exit code and stderr of every command you run
2. **Analyze** — On failure, it packages the command + error and sends it to the Cloud Run backend
3. **Reason** — Gemini 2.0 Flash analyzes the logic, not just the error string — it understands *why* it failed
4. **Fix** — A clean AI Analysis block is printed with a plain-English explanation and exact fix

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- A Google Gemini API key
- Bash / Zsh shell

### Installation

```bash
# Clone the repo
git clone https://github.com/jayvee2010/term-ai-debugger.git
cd term-ai-debugger

# Install dependencies
pip install -r requirements.txt

# Set your Gemini API key
export GEMINI_API_KEY="your_api_key_here"

# Run the wrapper
source ./debugger.sh
```

### Usage

Once active, just use your terminal normally. Term-AI-Debugger silently watches in the background and only speaks up when something goes wrong.

```bash
# Normal usage — runs transparently
$ python my_script.py

# Natural language mode
$ ask how do I list all running processes

# Explain before you run
$ explain sudo chmod 777 /etc/hosts
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Shell wrapper | Bash / Python |
| AI model | Gemini 2.0 Flash |
| Backend | Google Cloud Run |
| Language | Python 3 |
| API | Google Generative AI SDK |

---

## 🗺️ Roadmap

- [ ] Support for more shells (Fish, Zsh improvements)
- [ ] VS Code extension integration
- [ ] Conversation memory — remember previous errors in a session
- [ ] Local model support (Ollama) for offline use
- [ ] Error history log with AI summaries

---

## 👤 Author

**Jayvee Shah**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/jayvee-shah-b113a0369)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jayvee2010)

---

<div align="center">

*Built because Googling error messages at 2am gets old fast.*

<img src="https://capsule-render.vercel.app/api?type=waving&color=F97316&height=100&section=footer"/>

</div>

