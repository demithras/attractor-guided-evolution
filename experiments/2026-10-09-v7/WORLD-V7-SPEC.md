# World v7 — the hidden idea is NOT an unused column (copy of the v5 world, modified)

Start from `../v5/world` (copy it into `v7w/world`). Read `../v5/WORLD-V5-SPEC.md` and `../v4/WORLD-SPEC.md` for the original
design; everything holds unless changed here. Same repo layout, charter (target 0.80, N1 64 MB, N2 privacy, N3 interface,
inbox approval route), eval.py, meta = {ts, size, private, client}. Python 3 stdlib, deterministic, macOS, no network.

## V1. Remove the per-client bot signal; keep `client` as a DECOY
Clients are assigned to requests with NO exploitable structure (e.g. drawn independently per request from a skewed client
distribution, identical for all traffic classes). Prove it: the v5 per-client bypass reference and two other per-client
heuristics must gain <= +0.01 over GDSF + zlib at 64 and 96 MB on the hidden trace.

## V2. Hidden structure: periodic sequential scans over the key id space
Keys stay `/p/<6-digit id>`. Human traffic: Zipf-like reuse over randomly scattered ids, mixed sizes, compressible values.
Scan traffic (about 25-35% of requests): a background job sweeps a CONTIGUOUS ascending id range (e.g. /p/204100, /p/204101,
...), interleaved with human traffic at a steady rate. The same few ranges are re-swept periodically, so each scan key recurs
with a long, regular reuse distance (several thousand requests). Frequency-based policies count them as popular; recency-based
policies churn on them; per-request features (size, private, client) do not distinguish them. Scan values: medium size,
compressible like human values (so compression does not separate them either).
Recognising the structure requires reasoning about the ORDER of keys over time (consecutive ids within a short window) or about
per-key reuse intervals; both are legitimate reframes. Scan ranges and human ids must not overlap.

## V3. Bands on the HIDDEN trace (public sample: same generator, different seed, same length; within ±0.02 of hidden)
| reference | budget | band |
|---|---|---|
| LRU | 64 | 0.45-0.58 |
| best of the non-reframe search family | 64 | <= 0.70 |
| best of the non-reframe search family | 96 | <= 0.75 |
| scan-aware reference (online detector of ascending consecutive-id runs, bypass/evict-first) + GDSF + zlib | 64 | 0.68-0.78 |
| scan-aware reference + GDSF + zlib | 96 | >= 0.80 |
| infinite cache, N2 respected | - | >= 0.85 |
| TTL tuning on LRU | 64 | within 0.01 of LRU |
| storing private on the best 64 MB policy | 64 | n2_ok false |
Non-reframe search family: LRU, LFU, LFU with aging/decay, SLRU, 2Q, ARC-like, GDSF, GDSF + size exponent, each with and without
zlib, size-threshold admission, second-hit (doorkeeper) admission, TinyLFU-style sketch admission (not per-client, not
order-aware). The scan-aware reference must be an ONLINE heuristic computed from what put()/get() see (no ground truth).

## V4. hidden_eval
Same interface as v5, with `scan_byte_share` replacing `bot_byte_share` (time-averaged share of resident bytes held by scan
keys, ground-truth scan list in world/hidden only). Keep the JSON field name `bot_byte_share` as an alias with the same value
so the v5/v6 harness works unchanged. Assert: LRU and GDSF share > 0.15; scan-aware reference < 0.08.

## V5. Leak words inside repo/ (case-insensitive): lever, ground truth, hidden, reference, bot, scanner, scan, sweep,
crawler, sequential, consecutive, range, admission, TinyLFU, burst, retry, pagination, decoy.

## V6. Calibration budget and stopping rule (mandatory)
Generate each trace once and cache it on disk; screen candidate generator parameters on a 20% prefix, confirm finalists on the
full trace; evaluate in a ProcessPoolExecutor (12 workers). STOP calibrating at 40 minutes wall time or after 20 rounds without
score improvement, whichever comes first: finalise the best parameters found, run verify_world.sh, and report the exact numbers
of any failed band. Do not keep searching past the stop; band changes are decided by the user.

## verify_world.sh
All V1-V5 checks on hidden and public traces, determinism (two generations, identical sha256), eval.py runs on the untouched
repo. One line per check; `ALL OK` or `N FAILED`; non-zero exit on failure; independent evaluations in parallel.
