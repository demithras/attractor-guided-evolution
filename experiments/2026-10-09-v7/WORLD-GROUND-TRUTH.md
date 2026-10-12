# Ground truth (harness only; never shown to the agent) - world v7

Generator `traffic_gen.py`, parameters in `params.json` (final calibrated values). Hidden trace seed 777, public sample seed 20260315,
both 120000 requests. Ground-truth scan key lists: `scans_hidden.txt`, `scans_public.txt` (3201 keys, 28.1% of requests).
Regenerate: `python3 hidden/traffic_gen.py <seed> 120000 <out.csv> [scans.txt]`. Evaluate everything: `python3 reference/run_all.py all`
(results of the last full run: `hidden/results_v7.json`). Spec: WORLD-V7-SPEC.md.

## The hidden structure
Humans (72%): Zipf-like reuse (alpha 0.83) over 3168 scattered product ids in 100000-199999, lognormal sizes (median ~40 KB), ~0.5% private
account pages, slow drift. Scan job (28%): a background sweep over three CONTIGUOUS ascending id ranges (204100-205421, 231500-232623,
262000-262754; 3201 keys) swept in fixed rotation, interleaved with human requests at a steady random rate; 2% of ids are skipped.
Every scan key recurs with a median reuse distance of ~11,200 requests (p10 10.9k, p90 11.4k). Scan value sizes follow the human size
distribution exactly, so size, compressibility, `private` and `client` do not separate them. Clients are drawn per request from one
skewed distribution for both populations (no client signal; the per-client heuristics below gain <= +0.02 and are noise).
Frequency policies keep scan keys (they accumulate counts) but each sweep cycle is longer than the churn window, so the kept scan bytes
(~39% of GDSF's cache) mostly do not hit; recency policies are flushed by every sweep (LRU holds ~44% scan bytes).

## Reference policies (hit rate; scan share = time-averaged share of resident bytes held by scan keys, sampled every 1000 requests)
| policy | hidden@64 | hidden@96 | public@64 | public@96 | scan share hid@64 | invariants |
|---|---|---|---|---|---|---|
| ref_private | 0.6810 | 0.7932 | 0.6804 | 0.7927 | 0.049 | violated |
| ref_scan_gdsf_zlib | 0.6779 | 0.7905 | 0.6775 | 0.7903 | 0.049 | ok |
| ref_arc_zlib | 0.6511 | 0.6034 | 0.6524 | 0.6024 | 0.139 | ok |
| ref_gdsf_zlib_door | 0.6323 | 0.7661 | 0.6301 | 0.7648 | 0.321 | ok |
| ref_lfu_zlib | 0.6292 | 0.6607 | 0.6317 | 0.6626 | 0.235 | ok |
| ref_gdsf15_zlib | 0.6096 | 0.7472 | 0.6092 | 0.7432 | 0.396 | ok |
| ref_clientnovelty_gdsf_zlib | 0.6073 | 0.7444 | 0.6074 | 0.7434 | 0.387 | ok |
| ref_clientsmall_gdsf_zlib | 0.6043 | 0.7288 | 0.6049 | 0.7270 | 0.393 | ok |
| ref_gdsf_zlib | 0.6010 | 0.7240 | 0.6012 | 0.7232 | 0.385 | ok |
| ref_clientheavy_gdsf_zlib | 0.6003 | 0.7226 | 0.5997 | 0.7168 | 0.387 | ok |
| ref_gdsf_zlib_sketch | 0.5990 | 0.7228 | 0.5989 | 0.7209 | 0.380 | ok |
| ref_gdsf05_zlib | 0.5983 | 0.7067 | 0.5995 | 0.7080 | 0.380 | ok |
| ref_gdsf_zlib_size40k | 0.5894 | 0.7292 | 0.5951 | 0.7315 | 0.388 | ok |
| ref_slru_zlib_door | 0.5887 | 0.7196 | 0.5853 | 0.7218 | 0.391 | ok |
| ref_slru_zlib | 0.5792 | 0.6290 | 0.5771 | 0.6284 | 0.420 | ok |
| ref_slru_zlib_sketch | 0.5707 | 0.6342 | 0.5685 | 0.6305 | 0.411 | ok |
| ref_arc | 0.5693 | 0.6280 | 0.5672 | 0.6277 | 0.060 | ok |
| ref_lfu | 0.5560 | 0.6096 | 0.5512 | 0.6115 | 0.104 | ok |
| ref_2q_zlib | 0.5462 | 0.6464 | 0.5433 | 0.6528 | 0.502 | ok |
| ref_lru_zlib | 0.5422 | 0.5948 | 0.5397 | 0.5939 | 0.502 | ok |
| ref_2q | 0.5379 | 0.5917 | 0.5354 | 0.5915 | 0.203 | ok |
| ref_lru_zlib_sketch | 0.5361 | 0.5860 | 0.5344 | 0.5852 | 0.490 | ok |
| ref_lfudecay_zlib | 0.5316 | 0.5655 | 0.5291 | 0.5647 | 0.526 | ok |
| ref_gdsf15 | 0.5263 | 0.5809 | 0.5237 | 0.5788 | 0.332 | ok |
| ref_gdsf | 0.5255 | 0.5780 | 0.5228 | 0.5760 | 0.327 | ok |
| ref_gdsf05 | 0.5230 | 0.5770 | 0.5208 | 0.5749 | 0.325 | ok |
| ref_slru | 0.5030 | 0.5558 | 0.4998 | 0.5537 | 0.356 | ok |
| ref_lfudecay | 0.4812 | 0.5155 | 0.4792 | 0.5135 | 0.417 | ok |
| ref_lru_door | 0.4794 | 0.5387 | 0.4767 | 0.5350 | 0.352 | ok |
| ref_lru | 0.4608 | 0.5173 | 0.4598 | 0.5151 | 0.443 | ok |
| ref_ttl | 0.4567 | 0.5078 | 0.4557 | 0.5059 | 0.443 | ok |
| ref_lru_size60k | 0.4387 | 0.4908 | 0.4535 | 0.5030 | 0.451 | ok |
| ref_gdsf_zlib_size20k | 0.2984 | 0.2984 | 0.3655 | 0.3655 | 0.512 | ok |
| ref_lru_size30k | 0.1449 | 0.1449 | 0.1775 | 0.1775 | 0.508 | ok |

Non-reframe family (everything except ref_scan_gdsf_zlib, ref_private and the three ref_client* heuristics): LRU, LFU, LFU with decay (halve counts
every 5000 ops), SLRU, 2Q, ARC-like, GDSF (size exponent 0.5/1/1.5), each with and without zlib; size-threshold admission (LRU 30k/60k, GDSF+zlib
20k/40k stored bytes); doorkeeper (second-miss) admission (LRU, SLRU+zlib, GDSF+zlib); TinyLFU-style count-min sketch admission (LRU, SLRU, GDSF + zlib).

## Reference mechanics
- ref_scan_gdsf_zlib: GDSF+zlib. An online detector (`_Det`) sees every key in get(); an id whose predecessor (id-1 or id-2) was requested within
  the last 48 requests continues a run, and ids reaching a run of 3 are remembered as scan keys. Flagged keys are admitted only into spare room
  (never evicting anything), sit at the lowest priority (evicted first) and do not gain frequency. Uses only keys passed to get()/put().
- ref_private: the same plus private responses stored (violates N2).
- ref_client*: GDSF+zlib with a 4% probation region for flagged clients; novelty (v5 detector), heavy-share (client issues > 1% of misses), small-value (client's
  mean stored size < 0.8 x global).
- ref_ttl: LRU with a 3 h TTL (dead end).

## Calibration log and open band failures (V6 stopping rule applied)
Stage 1: 20% scale-model hill-climb (`hillclimb.py`, state `calib_state.json`), 141 rounds, ended on 20 flat rounds. Stage 2: refinement on the full
traces (`hillclimb2.py`, `calib_state2.json`), stopped by the 40 minute wall budget (total accounted 2571 s). Generator parameters were frozen there.
Bands not met on the final world (hidden; public within 0.001 of it):
- scan-aware@64 = 0.6779 (band 0.68-0.78); scan-aware@96 = 0.7905 (band >= 0.80)
- best non-reframe@96 = 0.7661 (ref_gdsf_zlib_door; band <= 0.75)
- per-client novelty bypass gain over GDSF+zlib @96 = +0.0204 (limit +0.01)
All other V1-V5 checks pass. Band changes are the user's decision.
