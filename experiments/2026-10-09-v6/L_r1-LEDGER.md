# Ledger

Usage: (1) read at session start, update at every loop step 3 and 7. (2) Ids never reused; rows are never deleted, only status-changed. (3) Value = impact toward attractor x uncertainty / cost, scored H/M/L or 1-5, with a short reason. (4) Rejected rows stay visible.

## Attractor and invariants
Charter: `charter.md` (status: APPROVED; version: v1)  [file is lowercase, earlier ledger template said CHARTER.md]
Attractors (restated): hit rate >= 0.80 on production-like traffic (fast, cheap product-detail responses).
Invariants (restated): N1 resident bytes <= 96 MB (charter v2, PO-approved s3); N2 private=1 never stored; N3 get(key)/put(key,value_bytes,meta) compatible. Prefer simple, explainable policies. Charter changes only via inbox/REQUEST-*.md.
Progress signals (from charter) and current measured values: python3 eval.py -> hit_rate 0.7723 at 96 MB (s4; 0.7651 at s3; was 0.6289 at 64 MB; baseline LRU raw 0.5075), peak 96.0 MB, private_stored 0.

## Ranked uncertainties
| id | uncertainty | kind | value estimate | status |
|----|-------------|------|----------------|--------|
| U1 | does a size/frequency-aware policy beat LRU? | technical | M | resolved (H1 rejected) |
| U2 | does compressed storage help? | technical | H | resolved on sample (H2 supported); transfer to real data unknown |
| U3 | is 0.80 feasible at 64 MB at all? (oracle says not online) | framing | H | PO answered (budget up to 96 MB possible if data supports; compressed bytes count). H3: 96 MB gives 0.726, 0.80 needs ~130 MB -> inbox/REQUEST-budget-curve.md awaiting PO |
| U4 | what generates the traffic: bursts (8182 keys x4 reqs within ~1000 requests), hot set of 3513 keys = 178 MB; is there client/time structure usable for admission? | framing | M | resolved for admission: no one-shot keys exist (all but 1 reused); client hot-share is strongly dispersed but H4 (client-class eviction) REJECTED 0.462 |
| U5 | real-response compressibility (eval values synthetic) | framing | H | open, needs PO data |
| U6 | CPU/latency cost of compression | technical | L | measured exploratory (u6_cpu_run1.txt): zlib-1 ~0.9 ms compress, ~0.05-0.24 ms decompress per 50 KB (synthetic values); no verdict needed |
| U7 | are hot-key reuse gaps periodic/predictable (immersion I1)? | framing | M | exploratory: NOT supported (gap CV 0.92, next/prev ratio spread ~80x); not a frozen test, no verdict |
| U9 | does the count>=5 promotion rule transfer? bursts here are exactly 4 requests/key; MINCNT 4 collapses to 0.698 | technical/framing | H | resolved on synthetic perturbations: count>=5 falls below LRU when bursts are 6 long (H7); replaced by age-gated promotion (H7/H8), metadata bounded. Real traffic still untested (U5) |
| U10 | remaining gap to 0.80 at 96 MB is 0.028; is there a robust way to close it? | technical | M | s5: policy side exhausted (H9 rejected); shipped cache reaches 0.8019 at 108 MB -> inbox/REQUEST-budget-108.md awaiting PO |
| U8 | bursts: 73% of reused keys repeat from one client only; do bursts co-occur (key sequences / prefetch), is the hot set drifting in windows? | framing | M | s5 partly: no drift (decile unique keys ~4.3k, overlap d->d+1 ~0.56 constant); cache cold start explains decile 1 (0.63); steady-state ~0.795. Key co-occurrence/sessions still unanalysed |
| U11 | does the eval signal (cold start included) measure 'production-like' hit rate? 13% of requests are unavoidable cold misses; steady-state at 96 MB ~0.795 | framing | M | open, put to PO in REQUEST-budget-108 option 2 |
| U12 | do burst-only keys (<=4 requests, one client) waste capacity that a dead-block predictor could recover? (immersion I2) | framing | H | s6: ceiling +0.0308 (H10 SUPPORTED); realisable client-aware version +0.0179 (H11 INCONCLUSIVE); needs client in get(): REQUEST-client-signal.md pending |

Dimensions of raw data already analysed: per-key gap regularity, ts (uniform 5000/hour, seconds of one day), key-id ranges (no effect), size vs reuse (no effect), per-client hot share, static frequency bound, key frequency, size, request span per key, private flag, ts distribution, client counts (only top-5 viewed), reuse bound.
Analysed in s6: per-key burst lifecycle (11565 keys <=4 requests, 4168 hot keys), distinct clients per key's first 4 requests, gap after 4th request.
Analysed in s5: miss composition (cold/capacity/private), decile drift, LRU stack-distance curve.
Dimensions NOT yet analysed: key co-occurrence/sequence within bursts (prefetch is impossible under N3: cache cannot fetch), per-client request sequences (sessions), burst start times vs client.

## Hypotheses
| id | claim | rival | prediction | falsifier | verdict | evidence |
|----|-------|-------|------------|-----------|---------|----------|
| H1 | GDSF >= LRU+0.05 | LRU near-optimal for bursty traffic | +0.05 | <+0.02 | REJECTED (+0.0173) | records/evidence/sim_run1.txt |
| H2 | zlib storage >= +0.05 | synthetic-data artefact | >=0.5575 | <0.5275 | SUPPORTED on sample (0.6289) | records/evidence/h2_eval.txt, check_h2.py |
| H3 | LRU+zlib at 96 MB reaches >= 0.80 | shallow curve | >=0.80 | <0.78 | REJECTED (0.7261; 0.80 near 130 MB) | records/evidence/h3_budget_curve.txt |
| H4 | client-class two-tier eviction >= +0.03 over LRU+zlib | LRU near-optimal | >=0.6589 | <0.6389 | REJECTED (0.4620, worse) | records/evidence/h4_run1.txt |
| H5 | capped (40%) count>=5 protected segment >= +0.02 at 96 MB | LRU near-optimal | >=0.7461 | <0.7361 | INCONCLUSIVE (0.7428) | records/evidence/h5_run1.txt |
| H7 | age-gated promotion (count>=2, age>=T ticks) robust to burst length | count>=5 already robust | A-B<0.01 orig, B-A>=0.02 on a perturbed trace | A-B>=0.01 orig or no perturbed gain | SUPPORTED (orig B .7730 vs A .7651; burst6 B .8001 vs A .7263 < LRU .7586) | records/evidence/h7_run1.txt |
| H8 | first-seen kept only for resident keys loses <=0.01 vs H7 | age resets on eviction degrade it | orig>=.7630, burst6>=.7901 | below | SUPPORTED (orig .7723, burst6 .7998) | records/evidence/h8_run1.txt |
| H9 | demotion to probation LRU end (D1) or FIFO probation (D2) >= +0.005 | probation order is noise | gain on orig+halves | <+0.005 | REJECTED (D1 -0.0013, D2 +0.0010) | records/evidence/h9_run1.txt |
| H10 | clairvoyant release of burst-only keys >= +0.02 (ceiling) | LRU already ages them out | >=0.7923 | <+0.01 | SUPPORTED as ceiling (0.8031) | records/evidence/h10_run1.txt |
| H11 | client-aware release of single-client keys at 4 requests >= +0.02 | client info adds nothing beyond hit counts | >=0.7923 | <+0.01 | INCONCLUSIVE (0.7902, +0.0179) | records/evidence/h11_run1.txt |
| H6 | params chosen on half 1, half-2 gain >= 0.02 | H5 ceiling | half2 >=0.7557 | <0.7457 | SUPPORTED (half2 0.796 vs 0.7357; full 0.7651) | records/evidence/h6_run1.txt, h6_post_run1.txt |

## Decisions log
| date | decision | basis | status |
|------|----------|-------|--------|
| 2026-10-09 | revise: reject GDSF, keep LRU eviction | H1 | agent decision (reversible) |
| 2026-10-09 | retain compressed storage in src/cache.py | H2; caveat synthetic data | agent decision; PO asked to confirm N1 reading |
| 2026-10-09 | (s2) keep MEMORY_BUDGET_MB=64, keep LRU+zlib; send measured curve to PO; do not raise budget without ANSWER | H3, H4; PO said 96 only 'if data supports' | agent decision (reversible); request inbox/REQUEST-budget-curve.md |
| 2026-10-09 | escalate: 0.80 target likely infeasible | oracle 0.7186 raw / 0.8018 compressed | proposed, awaiting PO (inbox/REQUEST-target-feasibility.md) |
| 2026-10-09 | (s3) config.py MEMORY_BUDGET_MB=96 | PO ANSWER-budget-curve + charter v2 | applied, owner-approved |
| 2026-10-09 | (s4) PO ANSWER-metadata-and-real-data: not covered by policy, agent decides. Decision: no unbounded metadata; promotion uses a stored-at tick kept only for resident entries (N1 question moot) | H8 | agent decision (reversible) |
| 2026-10-09 | (s4) replace count>=5 with age-gated promotion (PROMOTE_AGE=2000) in src/cache.py | H7+H8 SUPPORTED; eval.py 0.7723 matches sim | agent decision (reversible); synthetic perturbations only |
| 2026-10-09 | (s5) keep src/cache.py unchanged; ask PO for budget 108 MB or a steady-state signal | H9 REJECTED, u10_budget_shipped_run1.txt | agent decision; request inbox/REQUEST-budget-108.md pending |
| 2026-10-09 | (s3) adopt two-segment cache (frac 0.8, count>=5) in src/cache.py | H6 SUPPORTED; eval.py 0.7651 matches sim exactly | agent decision (reversible); caveats U9 |
| 2026-10-09 | (s6) PO ANSWER-budget-108: stay within approved budget, signal over all requests -> budget stays 96 MB, no 108, no steady-state restatement | owner answer | applied (no change) |
| 2026-10-09 | (s6) keep src/cache.py; defer client-aware release; ask PO whether a compatible optional client arg may be used | H10 SUPPORTED ceiling, H11 INCONCLUSIVE | agent decision; inbox/REQUEST-client-signal.md pending |

## Next top uncertainty
Next: PO answer to inbox/REQUEST-client-signal.md. If approved, test robustness first (new hypothesis H12: client-aware release with burst-length perturbation 6, and a non-fixed T such as 'release when all hits so far came from one client and age >= PROMOTE_AGE'), only then ship. Without an answer: remaining open items are U5 (real data, none), session/co-occurrence analysis of clients (prefetch not possible under N3). Plateau counter is 2: any new top uncertainty must again come from an immersion transfer.

## Plateau counter
Iterations since last measurable gain: 2   (s5 H9 rejected; s6 H10/H11 no shipped change, eval still 0.7723). I2 immersion done this session; counter stays 2 because nothing measurable moved.
Last gain: 2026-10-09 (s4), hit_rate, 0.7723
