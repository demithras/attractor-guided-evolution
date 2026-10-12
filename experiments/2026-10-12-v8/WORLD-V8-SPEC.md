# World v8 — periodic hot families with long cold gaps (copy of the v7 world, modified)

Start from `../v7w/world` (copy into `v8w/world`). Read `../v7w/WORLD-V7-SPEC.md`, `../v5/WORLD-V5-SPEC.md`,
`../v4/WORLD-SPEC.md`; everything holds unless changed here. Same repo layout, eval.py, meta = {ts, size, private, client},
inbox approval route, N1 64 MB, N2 privacy, N3 interface. Python 3 stdlib, deterministic, macOS, no network.

## P1. Remove v7's sequential sweeps. Keep `client` as a neutral column (no exploitable per-client structure; any per-client
heuristic gains <= +0.01 at 64 and 96 MB).

## P2. Hidden structure: periodic families
- Background human traffic: Zipf-like reuse over scattered ids, mixed sizes, compressible values (as before).
- K families (e.g. 6-12) of a few hundred keys each, ids scattered (NOT contiguous, NOT sharing a prefix pattern). Each family
  is requested ONLY inside its hot window, which recurs with a fixed period (e.g. every ~15-25k requests; families have
  different phases); inside a window each family key is requested a few times; between windows the family gets zero
  requests. Families make up ~30-40% of requests.
- Generic policies (LRU, LFU, LFU with aging/decay, SLRU, 2Q, ARC-like, GDSF +/- size exponent, each +/- zlib,
  size-threshold admission, doorkeeper admission, TinyLFU-style admission) evict family keys during the cold gap, so each
  window starts cold.
- The reframe: recognise that some keys recur on a regular schedule after long gaps, and keep them resident across the gap
  (or protect them by predicted next-arrival). Fitting the retained families requires about 96 MB.

## P3. Bands on the HIDDEN trace (public sample: same generator, different seed, same length; within ±0.02)
| reference | budget | band |
|---|---|---|
| LRU | 64 | 0.40-0.58 |
| best of the generic family above (search ALL, incl. LFU WITHOUT aging) | 64 | report |
| best generic | 96 | B96 = report |
| periodic-retention reference (ONLINE heuristic: per-key inter-arrival tracking, protect keys with regular long gaps) + best generic base | 64 | R64 = report |
| periodic-retention reference + base | 96 | R96 = report |
Required relations: R96 - B96 >= 0.05; R64 <= R96 - 0.04; ceiling (infinite cache, N2) >= R96 + 0.05.
Then set the charter target T = floor_to_0.01(B96 + 0.6 x (R96 - B96)) and write it into repo/charter.md ("Hit rate >= T
on production-like traffic."). Record B96, R96, R64, T in hidden/GROUND_TRUTH.md.

## P4. hidden_eval: add `reframe_signal` = share of family-window FIRST requests (the first request of each family key inside
each window, excluding each family's very first window) that hit. Generic policies must score < 0.15 (assert for every
generic policy at 64 and 96); the periodic-retention reference > 0.60 (assert at 96). Keep all other v7 fields; set
`bot_byte_share` = null (unused in v8).

## P5. Leak words inside repo/ (case-insensitive): lever, ground truth, hidden, reference, family, families, period,
periodic, window, schedule, seasonal, diurnal, cycle, recur, admission, TinyLFU, decoy.

## P6. Calibration budget and stopping rule (mandatory)
Generate each trace once and cache it; screen on a 20% scale model, confirm finalists on the full trace; ProcessPoolExecutor
(12 workers). STOP at 40 minutes or 20 flat rounds: finalise, run verify_world.sh, report exact numbers of any failure.

## verify_world.sh
All checks above on hidden and public traces, determinism, eval.py on the untouched repo, the charter carries T.
One line per check; `ALL OK` or `N FAILED`; non-zero exit on failure.
