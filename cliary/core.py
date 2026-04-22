from pathlib import Path
from datetime import datetime

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


def get_today_file():
    today = datetime.now().strftime("%Y-%m-%d")
    return LOG_DIR / f"{today}.txt"


def write_note():
    file = get_today_file()
    while True:
        note = input(">> ")
        if note.strip().lower() == 'exit': break
        with open(file, "a") as f:
            f.write(note + "\n")


def read_notes(slow_print):
    try: file = get_today_file() 
    except FileNotFoundError: ('No notes today')
    with open(file) as f:
        for line in f:
            slow_print(line)

def search_notes(keyword):
    for file in LOG_DIR.glob("*.txt"):
        with open(file) as f:
            for line in f:
                if keyword.lower() in line.lower():
                    print(f"{file.name}: {line.strip()}")
