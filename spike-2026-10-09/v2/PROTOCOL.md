# Spike protocol v2 (FROZEN 2026-10-09, before tasks were generated or any v2 run)
Same decision, H1, R1, H2, arms, model, reps, judge procedure and thresholds as v1 PROTOCOL.frozen.md, except:
1. Harness: every arm appends a no-tools instruction (notools.md); B/D append notools_age.md (= notools + AGE).
   Arms: A = --append-system-prompt-file notools.md ; B = notools_age.md ;
         C = --setting-sources project + notools.md ; D = --setting-sources project + notools_age.md
2. Tasks: 8 trap + 2 routine tasks, with keys and planted good/bad answers, written by a separate agent that has NOT
   read the AGE corpus and derives traps from real incidents in the user's ~/.claude/CLAUDE.md (+ general engineering).
   This favours the rival R1 (arm A carries those very rules).
3. Broken run = answer containing tool-call markup or < 150 chars on a trap. INVALID if > 2 broken per arm.
   Routine score = mean of 2 routine tasks; inflation rule unchanged (drop > 1 -> REJECTED).
Thresholds unchanged: SUPPORTED if trap mean diff >= 1.0 and no routine drop > 1; REJECTED if diff < 0.5; else INCONCLUSIVE.
