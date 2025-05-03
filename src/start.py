import os,subprocess,sys
from pathlib import Path

def start_server():
    script_path = Path(__file__).resolve().parent / "server.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)
