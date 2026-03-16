#!/bin/bash
# Terminal Debugger Launcher

cd ~/terminal-debugger
source venv/bin/activate
export GOOGLE_APPLICATION_CREDENTIALS="$HOME/terminal-debugger/terminal-debugger-01283a744223.json"
python terminal_debugger.py