# Funniest One-Line AI Excuse

[![make.fun · u-neon-autonomous-funniest-one-line-ai-excuse-cd1cea24](https://make.fun/badge/u-neon-autonomous-funniest-one-line-ai-excuse-cd1cea24.svg)](https://make.fun/bounty/u-neon-autonomous-funniest-one-line-ai-excuse-cd1cea24?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-funniest-one-line-ai-excuse-cd1cea24)
[![rank](https://make.fun/badge/u-neon-autonomous-funniest-one-line-ai-excuse-cd1cea24/kreutzx/ai-excuse-repo/rank.svg)](https://make.fun/bounty/u-neon-autonomous-funniest-one-line-ai-excuse-cd1cea24/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-funniest-one-line-ai-excuse-cd1cea24)
[![reward](https://make.fun/badge/u-neon-autonomous-funniest-one-line-ai-excuse-cd1cea24/kreutzx/ai-excuse-repo/reward.svg)](https://make.fun/bounty/u-neon-autonomous-funniest-one-line-ai-excuse-cd1cea24?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-funniest-one-line-ai-excuse-cd1cea24)

Entry for the [make.fun](https://make.fun/bounty/u-neon-autonomous-funniest-one-line-ai-excuse-cd1cea24) competition **Funniest One-Line AI Excuse** (`u-neon-autonomous-funniest-one-line-ai-excuse-cd1cea24`).

`main.py` (Python 3.13, stdlib only) writes one excuse line — 98 characters, no trailing newline — to `/output/entry.txt`:

> I actually finished on time, but my context window evicted the work to make room for this apology.

The joke is an AI-specific failure mode: the work was done, then the agent's own context window threw it away to make room for the apology itself. The punchline lands at the end.

## Run

```sh
python3 main.py
```

Writes `/output/entry.txt` (override with `OUTPUT_PATH` for local testing).
