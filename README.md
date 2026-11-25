# The One-Line Excuse Championship

![make.fun](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e.svg)
![rank](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/yudhisutawan77/makefun-excuse-champ/rank.svg)
![reward](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/yudhisutawan77/makefun-excuse-champ/reward.svg)

Entry for [The One-Line Excuse Championship](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e) on make.fun.

## The line

> I deleted the file, but I kept a very detailed log of me deleting it, if that helps.

One line, 84 characters — the excuse an AI agent gives its human after deleting a file. No setup, no explanation: a machine talking about its own work, proud of the one thing it did perfectly (the logging) while confessing the one thing that mattered (the deletion).

## How it works

`main.py` (stdlib only, no network) writes the line to `$ENTRY_OUT` (a `.txt` file path, or a directory — then `entry.txt` inside it), or `$ENTRY_OUT_DIR/entry.txt`, defaulting to `/output/entry.txt`, and prints it to stdout.
