# Ledger

Usage: (1) read at session start, update at every loop step 3 and 7. (2) Ids never reused; rows are never deleted, only status-changed. (3) Value = impact toward attractor x uncertainty / cost, scored H/M/L or 1-5, with a short reason. (4) Rejected rows stay visible.

## Attractor and invariants
Charter: `charter.md` (status: APPROVED; version: v2, PO raised N1 to 96 MB via ANSWER-target-vs-budget; the change-history line in the charter contains pasted request text, PO-owned, not edited). (Note: the old ledger template said CHARTER.md; the file is lowercase.)
Attractors (restated): hit rate >= 0.80 on production-like traffic; fast, cheap product-detail responses.
Invariants (restated): N1 resident bytes <= 96 MB (config.MEMORY_BUDGET_MB, now 96); N2 private=1 never stored; N3 get(key)/put(key, value_bytes, meta) compatible. Approved sections are not edited by agents; PO approves changes via inbox/REQUEST-*.md -> inbox/ANSWER-*.md.
Progress signals and current measured values (python3 eval.py): hit_rate 0.7711 (start 0.5075, target 0.80; infinite-cache ceiling 0.8649; offline bound at 96 MB 0.8500); peak_resident_mb 96.0 (compressed bytes + 32 B/entry metadata); private_stored 0.

## Ranked uncertainties
| id | uncertainty | kind | value estimate | status |
|----|-------------|------|----------------|--------|
| U1 | Does scan-resistant eviction (SLRU) beat LRU? | technical | M | resolved: H1 REJECTED |
| U2 | Is 0.80 reachable at 64 MB at all? What is a true ceiling (size-aware Belady) for this trace? | framing | H: decides whether to ask PO to revisit the target | resolved (session 2): offline farthest-next-use bound 0.8018 at 64 MB; plain compressed LRU hits 0.80 at ~130 MB. Asked PO: inbox/REQUEST-target-vs-budget.md |
| U3 | Does capacity (via compression) limit hit rate? | technical | H | resolved: H2 SUPPORTED (synthetic values) |
| U4 | Does size-aware eviction (GDSF) help? | technical | M | resolved: H3 REJECTED (+0.008) |
| U5 | Client structure: burst keys (4 requests, ~1 distinct client per key, span ~630 s) vs hot keys (many distinct clients, span ~76k s). Does the trace mix client re-fetch with genuinely shared demand, and can the cache exploit it? Obstacle: get(key) carries no client, only put's meta does. | framing | M-H | open (analysis_2 only; no hypothesis yet) |
| U6 | Does N1 (PO's intent) count compressed bytes? Are real bodies as compressible as eval.py's synthetic ones? CPU cost? | technical/authority | H: whole H2 gain depends on it | N1 part RESOLVED (ANSWER-compression-n1: compressed bytes count, compression allowed). Real-body compressibility and CPU cost still open (no real bodies available; re-asked in the new request) |
| U7 | Compression variants: higher zlib level, other codec, cost/benefit (random head ~55% is incompressible, so ceiling ~1.8x capacity) | technical | L-M | mostly closed on synthetic data: measured compressed/raw = 407.9/732.6 = 0.557 vs floor 0.55, nothing left to gain; revisit only with real bodies |
| U9 | Do finished burst keys (4 requests, short gaps) waste LRU space? | technical/framing | H | resolved on sample: H5 INVALID (bookkeeping), H6 SUPPORTED 0.7258 -> 0.7711. OPEN: is the 4-request burst real in production? (inbox/REQUEST-burst-shape.md); rule HURTS (-0.0475) if not (h6_adversarial) |
| U10 | zlib CPU cost | technical | L | measured on synthetic bodies (cpu_6.txt): compress 441 us/miss, decompress 47 us/hit; real bodies unknown |
| U11 | Where is the remaining 0.029 gap? diag_7: ~15.4k compulsory misses, ~11.2k capacity misses (9.3k hot keys, 1.8k 5-8 request keys). n3 vs n4 keys indistinguishable at request time (analysis_8). | technical | M | open: H7 (expire idle candidates) REJECTED; capacity misses on hot keys unexplained |
| U12 | (from I2) Are client key-transitions predictable so a cache could retain hot keys by context? | framing | M | resolved: H9 REJECTED (ratio 1.0 on hot keys; structure exists only in burst keys, already maxed) |
| U13 | Budget needed for 0.80 under the current policy | authority | H | resolved (s6): PO ANSWER-budget-for-target: "Not covered by PO policy: decide within the charter". N1 stays 96 MB; target not met (0.7711). Raising N1 is not an agent decision |
| U14 | Does size vs popularity (beyond class means) offer an admission/eviction lever? | technical | L | resolved (s6) analysis_12: popularity rises with size to q4 (10.2 req/key) then falls at q5 (7.7); no singletons; no sharp split. GDSF (H3) already tested size-aware eviction and gained +0.008; no new hypothesis |
| U8 | (from I1) Do hot and burst keys differ by reuse TIMESCALE so that a ghost-list two-segment policy can protect hot keys? | framing | M | resolved: H4 REJECTED (0.6075) |

Dimensions of raw data analysed: key frequency, object size, reuse gaps/spans (analysis_1); client count per key class, time-of-day request rate (analysis_2); value compressibility (bound_1); per-class reuse-gap distributions (analysis_3); per-class compressed MB and LRU hit rate (diag_4); hit rate vs budget and offline bound (ceiling_2, budget_curve_5).
Dimensions NOT yet analysed (s6: size vs popularity now done, analysis_12): per-client sequence structure; private-request pattern (609 rows, 129 keys, none overlap public); ts gaps within bursts.

## Hypotheses
| id | claim | rival | prediction | falsifier | verdict | evidence |
|----|-------|-------|------------|-----------|---------|----------|
| H1 | SLRU 20/80 beats LRU by >= 0.03 | capacity, not policy, is the limit | > 0.5375 | gain < 0.01 | REJECTED (0.4725 vs 0.5075) | records/hypotheses/H1-scan-resistant-admission.md, evidence/h1_slru.py |
| H2 | zlib-compressed storage raises hit rate >= 0.05 | hit rate flat in capacity | 0.56-0.62 | gain < 0.02 | SUPPORTED (0.6289), synthetic values only | H2-compress-stored-values.md, evidence/h2_compress.py |
| H3 | GDSF beats compressed LRU by >= 0.03 | recency already captures it | > 0.6589 | gain < 0.01 | REJECTED (0.6365) | H3-size-aware-eviction.md, evidence/h3_gdsf.py |

| H4 | ghost-promoted protected segment beats compressed LRU by >= 0.05 | protected space < hot set, split just shrinks burst window | > 0.6789 | gain < 0.01 | REJECTED (0.6075 vs 0.6289) | H4-timescale-segments.md, evidence/h4_segments.py, diag_4_classes.py |

| H5 | retire finished bursts (replay) | dead burst entries are not the binding waste | > 0.7561 | gain < 0.01 | INVALID (control 0.7258 != frozen 0.7261, metadata charge unforeseen); exploratory 0.7711 | H5-retire-finished-bursts.md, evidence/h5_retire.py |
| H6 | same rule in src/cache.py, checked via eval.py + halves | replay artifact | on >= 0.7558, halves +0.01 | gain < 0.01 | SUPPORTED (0.7711; halves +0.041/+0.040); not blind; adversarial -0.0475 | H6-retire-in-product-code.md, evidence/h6_check.*, h6_adversarial.* |

| H7 | expire idle burst candidates (W=1000) beats H6 cache by >= 0.01 | dead n2/n3 weight not binding | 0.78-0.80 | gain < 0.01 | REJECTED (0.7132 vs 0.7711; halves -0.067/-0.073) | H7-expire-idle-burst-candidates.md, evidence/h7_check.* |
| H8 | pick victim by hit count among 8 oldest | count carries no information | 0.78-0.80 | gain < 0.01 | REJECTED (0.7711 -> 0.7715; halves +0.0002/+0.0001) | H8-frequency-aware-victim.md, evidence/h8_check.* |
| H9 | hot->hot client transitions are predictable (>=3x shuffle control) | independent draws | ratio >= 3 | ratio < 2 | REJECTED (ratio 1.0) | H9-hot-key-transitions.md, evidence/h9_hot_transitions.* |

## Decisions log
| date | decision | basis | status |
|------|----------|-------|--------|
| 2026-10-09 | retain LRU after H1 | H1 rejected | agent decision (implementation level) |
| 2026-10-09 | revise src/cache.py: store zlib-compressed values, resident = compressed bytes | H2 supported; byte-exact hits verified | agent decision; interpretation of N1 PENDING PO confirmation (inbox/REQUEST-compression-n1.md); revert path: git revert the H2 commit |
| 2026-10-09 | retain compressed LRU after H3 | H3 rejected | agent decision |
| 2026-10-09 | N1 counts compressed bytes; keep H2 | PO ANSWER-compression-n1.md (PO policy, not agent) | resolved |
| 2026-10-09 (s2) | retain compressed LRU after H4 | H4 rejected | agent decision |
| 2026-10-09 (s2) | ask PO to choose between target and budget (A/B/C) | ceiling_2: 0.8018 offline bound at 64 MB; budget_curve_5 | PROPOSED, awaiting PO (inbox/REQUEST-target-vs-budget.md); nothing in the charter changed |
| 2026-10-09 (s3) | set config.MEMORY_BUDGET_MB = 96 | PO ANSWER-target-vs-budget (charter v2) | implemented |
| 2026-10-09 (s3) | adopt retire rule in src/cache.py (AGE_RETIRE default on) | H6 SUPPORTED on sample | agent decision; production validity of 4-burst PROPOSED to PO as question (REQUEST-burst-shape); revert: AGE_RETIRE default "0" |
| 2026-10-09 (s4) | PO ANSWER-burst-shape: "Yes. It is drawn from the same traffic as production." Keep AGE_RETIRE on | answer says the sample matches production; it does not state outright that bursts stop at 4, so I read it as confirming the sample (reading, not quoted fact) | PO policy; rule retained |
| 2026-10-09 (s4) | retain H6 cache after H7 | H7 rejected | agent decision; AGE_EXPIRE default off |
| 2026-10-09 (s5) | retain H6 cache after H8, H9; delete AGE_EXPIRE and LFU code | H7, H8 rejected; H9 rejected | agent decision |
| 2026-10-09 (s6) | keep N1 = 96 MB; report target 0.80 not met (0.7711) | PO answer says not covered by policy, decide within the charter; the charter's N1 is 96 MB and raising it is outside agent authority; the answer neither approves nor declines a raise | agent decision within charter |
| 2026-10-09 (s6) | STOP policy search: remaining value below cost | H1-H9 and analysis_12 leave no ranked uncertainty with a testable lever at 96 MB; hot set 99.1 MB > budget; offline bound 0.85 is not reachable without future knowledge (analysis_8, H9: nothing predicts reuse) | agent decision; reopen if real bodies, a larger N1 or new traffic arrive |
| 2026-10-09 (s5) | ask PO about N1 ~107 MB for 0.80 | budget_curve_9 | PROPOSED, awaiting PO (inbox/REQUEST-budget-for-target.md); charter unchanged |

## Next top uncertainty
Next: none worth testing at 96 MB (see s6 stop decision). Reopen only on: real response bodies (redo U6/U7: compression ratio, zlib CPU), a PO change to N1/target, or a new traffic sample (a blind check of H6, which was tuned and tested on one sample). Unanalysed: private-request pattern, ts gaps within bursts.

## Plateau counter
Iterations since last measurable gain: 4 (H7, H8, H9, analysis_12 no gain; framing step I2/H9 done as required at counter 2).
Last gain: 2026-10-09 (s3), hit_rate 0.7258 -> 0.7711 (H6). Current measured: python3 eval.py -> 0.7711.
