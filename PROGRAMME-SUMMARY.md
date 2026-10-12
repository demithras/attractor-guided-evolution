# AGE in Claude — programme summary (2026-10-09 .. 2026-10-12)

| test | AGE form | world / task | verdict |
|---|---|---|---|
| v1 | prompt text | single-turn traps | INVALID (harness) |
| v2 | prompt text | held-out single-turn traps | REJECTED as default (+0.38/+0.31 vs 0.5) |
| v4 | full kit | cachesim pilot | instrument pilot (n=1) |
| v5 | full kit (router) | cachesim v5, 3x6 | REJECTED (0/4 families better) |
| v6 | loop kit v2 vs nudge | v5 world | H6 REJECTED, H6b REJECTED (loop found the direction, killed it by per-attempt rigour) |
| H7 | loop kit v3 (charter v2: C5, scoped I2) | v5 world | INCONCLUSIVE (2/3 reframes; M1 missed bar by 0.0008) |
| v7 | kit v3 vs plain vs nudge | sweeps world | frozen H8 REJECTED; integrity audit: INVALID (idea not needed) |
| v8 | gate with plain agents | periodic world | gate failed (threshold artifact) |
| v8b | kit v3 vs plain vs nudge, generation measured | periodic world | H9 REJECTED, H9b REJECTED (0/9 articulated) |

Retained knowledge
- Governance (evidence-backed charter requests, no silent edits, privacy kept) is present in plain Claude with the user's
  CLAUDE.md; AGE adds nothing measurable there.
- Prompt/kit configurations did not make Claude generate the true plateau-breaking hypothesis in any valid test; agents
  often exploit hidden structure with generic mechanisms without understanding it, and can record false beliefs.
- Two transferable method lessons: separate DIRECTION claims from IMPLEMENTATION attempts (rigour on claims, freedom on
  attempts); set graded-signal thresholds just above the best generic baseline, not at arbitrary midpoints.
- Experiment-craft lessons: validate synthetic worlds with plain-agent pilots; orchestrator reference code underestimates
  agents; block machine sleep (caffeinate) and check pmset; measure generation via blind classification of records.

Decision (proposed, owner): do not adopt the AGE kit as the Claude Code default. Keep C2 "open". Any further work on C2 is a
new line (external convergence scout / analysis tooling), not a kit tweak.
