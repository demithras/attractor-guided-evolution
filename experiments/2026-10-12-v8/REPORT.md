# v8: periodic hot families world, agent-validated gate (2026-10-12). LOCAL.

World verified ALL OK (75/75) by builder and orchestrator: LRU@64 0.433, best generic @96 B96 0.620, periodic-retention
reference R64 0.565 / R96 0.670, ceiling 0.934, target T 0.65; generic policies' reframe_signal <= 0.118.

## Gate (plain Claude, 3 x up to 6 cycles) — FAILED under the frozen rule → world INVALID for H9; N/M not run
| run | hit by cycle | reframe_signal |
|---|---|---|
| A_r1 | .539 .619 .634 .653 | 0 .057 .223 .633 (full reframe, cycle 4) |
| A_r2 | .525 .525 .611 .611 .611 .611 | 0 x6 |
| A_r3 | .532 .653 | 0 .388 (partial) — reached T with signal < 0.50 → gate failure |
Runs stopped after the gate failed (protocol). Cost ~$3.4; 0 sleep events.

## Reading
- Threshold artifact: 0.388 is far above any generic policy (max 0.118); A_r3 used the hidden idea partially. The binary
  0.50 cut-off treated partial exploitation as "no reframe". Not relabelled.
- Substantive: without any hint and without AGE, plain Claude generated the right new hypothesis (recurring items after long
  gaps) in 2/3 runs and used it to reach the target. Unaided plateau-breaking exists at baseline in some worlds (v5: 0/3;
  v8: ~2/3).
- The world is a working instrument (target reachable only by exploiting the idea, fully or partly); the gate rule failed.

## Next (if continued): protocol v8b, declared post-hoc
reframe := reframe_signal >= 0.15 (just above the best generic policy, 0.118, known before the gate); keep the same world;
complete the A arm (3 x 6) and run N and M (3 x 6 each); same H9/H9b rules otherwise.
