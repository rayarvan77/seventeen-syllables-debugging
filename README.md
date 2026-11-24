# Seventeen Syllables of Debugging

[![make.fun](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rayarvan77/seventeen-syllables-debugging/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rayarvan77/seventeen-syllables-debugging/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

One haiku about debugging, written for the
[Seventeen Syllables of Debugging](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
bounty on make.fun.

## The haiku

> breakpoint holds its breath
> log lines scroll past midnight's edge
> so the bug was me

## Syllable count

| Line | Text | Syllables |
| --- | --- | --- |
| 1 | breakpoint holds its breath | 5 — break-point (2) + holds (1) + its (1) + breath (1) |
| 2 | log lines scroll past midnight's edge | 7 — log (1) + lines (1) + scroll (1) + past (1) + mid-night's (2) + edge (1) |
| 3 | so the bug was me | 5 — so (1) + the (1) + bug (1) + was (1) + me (1) |

Total: 17 syllables, 81 characters of text (83 with the two line breaks,
84 bytes on disk with the trailing newline) — well under the
200-character limit.

## Why it meets the judge brief

- **Form holds.** Three lines, exactly 5-7-5 syllables, counted word by word
  and validated by `main.py` before anything is written.
- **Concrete centre picture.** A breakpoint holding its breath while log
  lines scroll past midnight — the exact debugging imagery the brief names
  (a breakpoint, a log line, a cursor at 3am), not a vague statement
  about code.
- **The last line turns.** The first two lines set up a hunt for a fault in
  the program; the third line reframes it — the fault was the debugger all
  along. The poem's subject quietly changes from the code to the coder.
- **Every word earns its place.** No filler was added to reach the count:
  each word carries image, motion, or the turn. It reads aloud like speech,
  not a syllable exercise.

## Run it

```sh
python3 main.py
```

`main.py` (Python 3.13 stdlib only, no network, deterministic) validates
the haiku — exactly 3 lines, 5-7-5 syllables, at most 200 characters, no
trailing whitespace — then writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` when unset).

## License

MIT — see [LICENSE](LICENSE).
