import argparse
import time
from cliary.core import write_note, read_notes, search_notes


def slow_print(text):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(0.02)
    print()


def main():
    parser = argparse.ArgumentParser(prog="snaplog")
    parser.add_argument("command")
    parser.add_argument("arg", nargs="?")
    args = parser.parse_args()
    
    match args.command:
        case "write": write_note()
        case "read": read_notes(slow_print)
        case "search": search_notes(args.arg) if args.arg else print('Please provide a keyword')
