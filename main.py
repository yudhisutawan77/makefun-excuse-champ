import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

CHAMPION_LINE = "I deleted the file, but I kept a very detailed log of me deleting it, if that helps."


def _champion_line():
    return CHAMPION_LINE


def _entry_target():
    explicit = os.environ.get("ENTRY_OUT")
    if explicit:
        if explicit.endswith(".txt"):
            return explicit
        return os.path.join(explicit, "entry.txt")
    folder = os.environ.get("ENTRY_OUT_DIR")
    if folder:
        return os.path.join(folder, "entry.txt")
    return "/output/entry.txt"


def _persist_line(line, target):
    directory = os.path.dirname(target)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(target, "w", encoding="utf-8") as sink:
        sink.write(line + "\n")


def run():
    line = _champion_line()
    _persist_line(line, _entry_target())
    print(line)


if __name__ == "__main__":
    run()
