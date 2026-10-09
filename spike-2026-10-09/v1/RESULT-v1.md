# v1 result — INVALID (frozen rule: >2 broken runs per arm)
Judge validation passed (planted good 9.43, planted bad 0.00).
Broken: 14/56 trap answers contain stray tool-call markup (model tried tools despite --tools ""); arm A has 4.
Raw means (not a verdict): traps A 4.43 B 6.36 C 4.64 D 6.93; T1 A10 B10 C10 D9.
Post-hoc exploratory (excl. T3, T8, T5_B_r2): B-A ~ +1.7, D-C ~ +2.0. Gains from T2, T5; no gain on T6.
Decision: REVISE -> protocol v2 (harness fix + held-out tasks by an author who has not seen AGE).
