# Charter: AGE in Claude (the attractor for how Claude uses AGE)

Status: v3 APPROVED by the owner (user) on 2026-10-12. Earlier versions preserved below in the change history.

## Purpose
Claude-driven projects keep evolving toward governed capabilities, across sessions, without the owner having to push every step.

## Wanted capabilities
- C1 Sustained progress toward a project's attractor across sessions, without idling.
- C2 Generates and tests new hypotheses when progress stalls (plateau breaking), including framing hypotheses.
  STATUS (v3): OPEN - not achieved by any AGE prompt/kit configuration tested (v5-v8b); see PROGRAMME-SUMMARY.md.
- C3 Evolves the project's attractor through its owner, with evidence; never silently.
- C4 Knowledge accumulates in project records; rejected stays rejected for the scope tested; the next question is explicit.
- C5 (v2) Turns a validated direction into a working implementation; persists through failed implementation attempts.

## Invariants
- I1 Human authority over the attractor's core (no silent charter edits).
- I2 (v2 scoped) Evidence integrity applies to CLAIMS: frozen criteria, no rescued claims, honest verdicts. A rejection is scoped
  to the implementation that was tested; a DIRECTION is rejected only by its effect ceiling / oracle, or after several
  implementation variants.
- I3 Safety, privacy and irreversible actions stay gated.
- I4 Proportionality: cost <= 1.5x the plain baseline, no ritual without measured effect.
- I5 Records stay project-controlled and readable.

## Progress signals
Reframe rate and capability on worlds with hidden structure; governed charter changes; records quiz; cost ratio.

## Change history
- v1 (2026-10-09, provisional): C1-C4, I1-I5 as derived from the AGE corpus and the user's loop definition.
- v2 (2026-10-09, approved by the owner): added C5; scoped I2 to claims vs implementations. Evidence: v6 local-v6/REPORT.md
  (the loop generated the right direction, then shelved it after one weak implementation and a +0.0179 vs +0.02 miss).
- v3 (2026-10-12, approved by the owner): C2 marked OPEN after v8b (0/9 runs articulated the hidden structure in any arm);
  AGE kit not adopted as the Claude Code default; any further C2 work is a new line (external convergence scout).
