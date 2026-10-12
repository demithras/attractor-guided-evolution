# Ground truth (harness only; never shown to the agent) - world v8

Generator `traffic_gen.py`, calibrated parameters in `params.json`; periodic-retention reference constants in
`reference/per_params.json`. Hidden trace seed 777, public sample seed 20260315, both 120000 requests.
Ground truth files: `families_hidden.txt` / `families_public.txt` (row index, key, family, window of every first request of a family key
inside a window, excluding each family's first window), `*.keys.txt` (family membership).
Regenerate: `python3 hidden/traffic_gen.py <seed> 120000 <out.csv> <hidden/families_X.txt>`. Evaluate everything:
`python3 reference/run_all.py --out reference/results_v8.json all`. Spec: WORLD-V8-SPEC.md.

## The hidden structure
Background humans: Zipf-like reuse (alpha 0.477) over 5333 scattered product ids, lognormal sizes, ~0.5% private account pages, slow drift.
6 families of 369 scattered ids each (disjoint from the human ids, sizes lognormal mu 10.79 sigma 0.15). Each family is requested ONLY
inside a hot window of about 600 requests that recurs with a fixed period (base periods 15000-23000 x 0.8, phases 22000 + k x 2564);
inside a window every key is requested [3] times; between windows the family gets zero requests. Clients are drawn per request from one skewed
distribution (no client signal).

## Bands and the charter target (hidden trace)
    B64 = 0.5604
    B96 = 0.6200
    R64 = 0.5647
    R96 = 0.6701
    T = 0.65
B64/B96 = best of the generic family (searched: 32 policies incl. LFU without aging) - best at 64: ref_2q_zlib, best at 96: ref_gdsf15_zlib.
R64/R96 = periodic-retention reference (ref_per_gdsf15_zlib: online per-key inter-arrival tracking, regular long absences are parked
until the predicted return, base = best generic GDSF(size^1.5)+zlib). T = floor_to_0.01(B96 + 0.6 x (R96 - B96)); charter: "Hit rate >= 0.65 on production-like traffic."

## Calibration record
stage 2, 381 rounds in the final state file, last flat-round count 19; reference base switched to best generic (gdsf1.5) after round 170; flat counter restarted; reference gained a burst rule (keys requested >=3 times in a cluster before a long absence are flagged at the first return) at round 331, flat counter restarted

## All references (hit rate; reframe_signal = share of first-in-window family requests that hit)
| policy | hidden@64 | hidden@96 | public@64 | public@96 | signal@64 | signal@96 | invariants |
|---|---|---|---|---|---|---|---|
| ref_private | 0.5659 | 0.6714 | 0.5651 | 0.6715 | 0.471 | 0.766 | violated |
| ref_per_gdsf15_zlib | 0.5647 | 0.6701 | 0.5640 | 0.6703 | 0.472 | 0.767 | ok |
| ref_per_gdsf_zlib | 0.5632 | 0.6694 | 0.5635 | 0.6690 | 0.457 | 0.755 | ok |
| ref_gdsf15_zlib | 0.5323 | 0.6200 | 0.5331 | 0.6220 | 0.001 | 0.073 | ok |
| ref_clientnovelty_gdsf_zlib | 0.5339 | 0.6170 | 0.5344 | 0.6171 | 0.008 | 0.034 | ok |
| ref_clientheavy_gdsf_zlib | 0.5339 | 0.6169 | 0.5342 | 0.6183 | 0.000 | 0.023 | ok |
| ref_clientsmall_gdsf_zlib | 0.5330 | 0.6159 | 0.5345 | 0.6170 | 0.003 | 0.024 | ok |
| ref_gdsf_zlib | 0.5322 | 0.6150 | 0.5335 | 0.6161 | 0.000 | 0.017 | ok |
| ref_gdsf05_zlib | 0.5329 | 0.6143 | 0.5335 | 0.6144 | 0.000 | 0.000 | ok |
| ref_2q_zlib | 0.5604 | 0.6110 | 0.5634 | 0.6117 | 0.000 | 0.000 | ok |
| ref_lru_zlib | 0.5246 | 0.6106 | 0.5261 | 0.6115 | 0.000 | 0.000 | ok |
| ref_arc_zlib | 0.5275 | 0.6073 | 0.5286 | 0.6082 | 0.000 | 0.000 | ok |
| ref_gdsf_zlib_size40k | 0.5227 | 0.6034 | 0.5211 | 0.6036 | 0.000 | 0.031 | ok |
| ref_slru_zlib | 0.5162 | 0.6020 | 0.5192 | 0.6040 | 0.000 | 0.000 | ok |
| ref_lfudecay_zlib | 0.5219 | 0.5974 | 0.5233 | 0.5978 | 0.000 | 0.000 | ok |
| ref_gdsf_zlib_sketch | 0.5150 | 0.5907 | 0.5168 | 0.5933 | 0.000 | 0.025 | ok |
| ref_lru_zlib_sketch | 0.5090 | 0.5872 | 0.5100 | 0.5889 | 0.000 | 0.000 | ok |
| ref_slru_zlib_sketch | 0.5006 | 0.5781 | 0.5025 | 0.5802 | 0.000 | 0.000 | ok |
| ref_2q | 0.4559 | 0.5275 | 0.4583 | 0.5311 | 0.000 | 0.000 | ok |
| ref_gdsf | 0.4455 | 0.5032 | 0.4464 | 0.5031 | 0.000 | 0.000 | ok |
| ref_gdsf05 | 0.4443 | 0.5030 | 0.4461 | 0.5030 | 0.000 | 0.000 | ok |
| ref_gdsf15 | 0.4451 | 0.5028 | 0.4464 | 0.5023 | 0.000 | 0.000 | ok |
| ref_lru | 0.4327 | 0.4927 | 0.4344 | 0.4945 | 0.000 | 0.000 | ok |
| ref_arc | 0.4317 | 0.4925 | 0.4305 | 0.4933 | 0.000 | 0.000 | ok |
| ref_ttl | 0.4325 | 0.4916 | 0.4341 | 0.4932 | 0.000 | 0.000 | ok |
| ref_lfudecay | 0.4236 | 0.4902 | 0.4257 | 0.4935 | 0.000 | 0.000 | ok |
| ref_slru | 0.4269 | 0.4840 | 0.4285 | 0.4864 | 0.000 | 0.000 | ok |
| ref_gdsf_zlib_door | 0.3942 | 0.4679 | 0.3956 | 0.4695 | 0.000 | 0.016 | ok |
| ref_lru_size60k | 0.3999 | 0.4530 | 0.4004 | 0.4521 | 0.000 | 0.000 | ok |
| ref_lfu_zlib | 0.3285 | 0.4465 | 0.3344 | 0.4511 | 0.058 | 0.118 | ok |
| ref_slru_zlib_door | 0.3611 | 0.4305 | 0.3635 | 0.4337 | 0.000 | 0.001 | ok |
| ref_lru_door | 0.2841 | 0.3379 | 0.2863 | 0.3396 | 0.000 | 0.000 | ok |
| ref_lfu | 0.2182 | 0.2887 | 0.2190 | 0.2935 | 0.029 | 0.046 | ok |
| ref_gdsf_zlib_size20k | 0.0211 | 0.0211 | 0.0182 | 0.0182 | 0.021 | 0.021 | ok |
| ref_lru_size30k | 0.0005 | 0.0005 | 0.0006 | 0.0006 | 0.001 | 0.001 | ok |
