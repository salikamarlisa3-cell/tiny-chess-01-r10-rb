# tiny-chess-01 R10 (Ruang Build) — Verified Mate Book, Trap-Beam Edition

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/salikamarlisa3-cell/tiny-chess-01-r10-rb/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/salikamarlisa3-cell/tiny-chess-01-r10-rb/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A sub-4 KB Python chess entry for make.fun's tiny-chess-01. The book
holds 18 forced-mate lines found by trap-style beam search against the
house engines' exact replies and re-verified by full oracle replay
(579 plies total; practice spare 1013 / 1007 / 1001). A PeSTO-evaluated
alpha-beta engine with a fixed node budget plays everything else.
`main.py` is the whole engine, produced from `src_rb.py` by the kit's
compress step.

## License

MIT — see LICENSE.
