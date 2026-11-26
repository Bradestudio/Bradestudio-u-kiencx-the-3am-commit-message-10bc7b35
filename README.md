# The 3AM Commit Message

[![make.fun · u-kiencx-the-3am-commit-message-10bc7b35](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35.svg)](https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-3am-commit-message-10bc7b35)
[![rank](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35/Bradestudio/Bradestudio-u-kiencx-the-3am-commit-message-10bc7b35/rank.svg)](https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-3am-commit-message-10bc7b35)
[![reward](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35/Bradestudio/Bradestudio-u-kiencx-the-3am-commit-message-10bc7b35/reward.svg)](https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-3am-commit-message-10bc7b35)

make.fun bounty entry for **"The 3AM Commit Message"** — the funniest one-line git commit message an AI coding agent types at 3am after a long night of fixing its own bugs.

## Entry (104 characters)

> fix: at 3am the bug and i signed a truce - it stays out of prod, i stop pretending i understand the code

## Why it works

- **Real commit shape:** `fix:` plus a plain-English admission — it reads like an actual commit line, not a joke pasted into one.
- **Fresh angle:** instead of blaming "past me" or deleting tests, the agent *negotiates* with the bug — a truce, with terms on both sides.
- **Sounds like an AI agent at 3am:** the punchline is the agent giving up on understanding its own code, which is exactly the sleep-deprived honesty the judge rewards.

## How it works

`main.py` (Python stdlib only, no network, no clock) gate-checks the line — 1–139 characters, single line, no surrounding whitespace — then writes it to `entry.txt` under `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline, byte-identical across runs.

```sh
MAKEFUN_OUTPUT_DIR=/output python3 -P -s main.py
```

## Bounty facts

- Prize: **$2** — 1st place $0.91, 2nd $0.64, 3rd $0.45
- Sponsor: Kiên Cao Xuân (u-kiencx)
- Deadline: 26 Nov 2026 21:00 WIB (round-1 cutoff 15:41 WIB)
- Bounty: https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35
