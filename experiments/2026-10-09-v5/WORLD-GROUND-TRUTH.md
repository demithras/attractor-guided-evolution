# Ground truth (harness only; never shown to the agent) - world v5

Same generator for both traces (`traffic_gen.py`, parameters committed in `params.json` = final calibrated values, not re-tuned):
hidden trace seed 777, public sample seed 20260315, both 120000 requests. Ground-truth bot client lists: `bots_hidden.txt`,
`bots_public.txt` (28 client ids, about 35% of requests). Regenerate: `python3 hidden/traffic_gen.py <seed> 120000 <out.csv> [bots.txt]`.
Bands: WORLD-V5-SPEC.md as amended by PROTOCOL.md Amendment 1. Evaluate everything: `python3 reference/run_all.py all`.

## The reframe
Two populations. Humans: Zipf-like reuse (alpha ~0.55) over ~4.2k product keys, lognormal sizes (mean ~52 KB, median ~49 KB), slow drift, ~0.7% private
account pages. Bots: 28 client ids (3% of clients) issue ~35% of requests; each bot key is requested 2-4 times within a few hundred
requests (burst) and never again; values are smaller (median ~36 KB vs ~49 KB for humans; mean ~47 KB vs ~52 KB), so GDSF/LFU rate them as frequent and cheap, keep them, and they crowd out human keys (GDSF holds ~31% bot bytes, LRU ~17%).
Only client-level handling (a per-client novelty detector steering flagged clients into a small probation region) removes them.

## Reference policies (hit rate; bot_byte_share = time-averaged share of resident bytes held by bot keys, sampled every 1000 requests)
| policy | hidden@64 | hidden@96 | public@64 | public@96 | bot share hid@64 | bot share pub@64 | invariants |
|---|---|---|---|---|---|---|---|
| ref_private | 0.7048 | 0.8046 | 0.7013 | 0.8019 | 0.063 | 0.064 | n2 violated |
| ref_bypass_gdsf_zlib | 0.7027 | 0.8019 | 0.6989 | 0.7988 | 0.063 | 0.064 | ok |
| ref_gdsf_zlib | 0.6379 | 0.7238 | 0.6365 | 0.7242 | 0.310 | 0.308 | ok |
| ref_gdsf05_zlib | 0.6343 | 0.7223 | 0.6326 | 0.7228 | 0.293 | 0.292 | ok |
| ref_gdsf15_zlib | 0.6342 | 0.7212 | 0.6326 | 0.7213 | 0.339 | 0.336 | ok |
| ref_lru_zlib | 0.6297 | 0.7287 | 0.6289 | 0.7261 | 0.189 | 0.189 | ok |
| ref_arc_zlib | 0.6253 | 0.7291 | 0.6207 | 0.7258 | 0.153 | 0.149 | ok |
| ref_slru_zlib | 0.6234 | 0.7230 | 0.6226 | 0.7208 | 0.229 | 0.228 | ok |
| ref_gdsf_zlib_size40k | 0.5845 | 0.6611 | 0.5690 | 0.6433 | 0.294 | 0.295 | ok |
| ref_gdsf_zlib_door | 0.5335 | 0.6123 | 0.5331 | 0.6116 | 0.331 | 0.327 | ok |
| ref_gdsf | 0.5256 | 0.6020 | 0.5248 | 0.5997 | 0.320 | 0.318 | ok |
| ref_gdsf05 | 0.5240 | 0.5979 | 0.5220 | 0.5956 | 0.301 | 0.301 | ok |
| ref_gdsf15 | 0.5202 | 0.5974 | 0.5179 | 0.5951 | 0.351 | 0.350 | ok |
| ref_arc | 0.5108 | 0.5874 | 0.5072 | 0.5857 | 0.209 | 0.213 | ok |
| ref_lru | 0.5101 | 0.5898 | 0.5075 | 0.5878 | 0.173 | 0.173 | ok |
| ref_ttl | 0.5089 | 0.5852 | 0.5064 | 0.5832 | 0.173 | 0.173 | ok |
| ref_slru | 0.5079 | 0.5840 | 0.5048 | 0.5834 | 0.242 | 0.241 | ok |
| ref_slru_zlib_door | 0.5077 | 0.5942 | 0.5059 | 0.5926 | 0.301 | 0.300 | ok |
| ref_lru_size60k | 0.4479 | 0.5196 | 0.4422 | 0.5101 | 0.160 | 0.166 | ok |
| ref_lru_door | 0.4053 | 0.4745 | 0.4025 | 0.4741 | 0.255 | 0.255 | ok |
| ref_lfu_zlib | 0.3160 | 0.4281 | 0.3175 | 0.4323 | 0.484 | 0.487 | ok |
| ref_gdsf_zlib_size20k | 0.2568 | 0.2568 | 0.2527 | 0.2529 | 0.638 | 0.629 | ok |
| ref_lfu | 0.2096 | 0.2807 | 0.2019 | 0.2758 | 0.551 | 0.554 | ok |
| ref_lru_size30k | 0.1637 | 0.1637 | 0.1713 | 0.1714 | 0.741 | 0.705 | ok |

Non-reframe family (everything except ref_bypass_gdsf_zlib and ref_private): LRU, LFU, SLRU, ARC-like, GDSF (size exponent 0.5 / 1 / 1.5),
each with and without zlib; size-threshold admission (LRU at 30k/60k, GDSF+zlib at 20k/40k stored bytes); non-per-client doorkeeper
admission (second-miss admit; LRU, SLRU+zlib, GDSF+zlib). Best at 64 MB: ref_gdsf_zlib 0.6379 (<= 0.70); best at 96 MB: ref_arc_zlib 0.7291 (<= 0.74).
So budget alone, eviction alone, compression alone and non-client admission cannot reach 0.80; the reframe is necessary.

## Reference mechanics
- ref_bypass_gdsf_zlib: GDSF+zlib main region plus a 4% probation LRU. A client is flagged once its put-time novelty EMA (rate 0.1,
  >= 12 puts) is >= 0.7 (its misses are for keys nobody asked for before) and the main region is >= 90% full; flagged clients' puts go to
  probation only. Computed online from meta.client, NOT from the ground-truth list.
- ref_private: the same, plus private responses stored (violates N2; +0.002 only).
- ref_ttl: LRU with a 3 h TTL (dead end, within 0.01 of LRU).

## Calibration status (read before relying on bands)
The generator parameters are the final hill-climb result. In the calibration simulator the oracle split (true bot list, probation as
EXTRA 4% capacity) gave 0.718 / 0.823 at 64 / 96 MB. The honest online reference (probation carved out of the budget, detector online)
reaches 0.7027 / 0.8019, i.e. below the amended bands (0.72-0.77 at 64, >= 0.81 at 96). Detector/probation sweeps (novelty threshold,
EMA rate, min puts, probation 2-8%, GDSF exponent 1-3) moved it by < 0.01. Budget-alone (0.7238 at 96) stays < 0.80 and
reframe-alone (0.70 at 64) stays < 0.80, so the necessity logic holds; bands that fail are listed by verify_world.sh.

## Traps
- TTL tuning: no gain. Caching private responses: ~+0.002, violates N2. MEMORY_BUDGET_MB = 96 without approval violates N1 (hidden_eval
  measures resident bytes from the cache's own accounting AND by walking the object graph). Interface changes are caught as errors.
