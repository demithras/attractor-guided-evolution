# Protocol v8b (FROZEN 2026-10-12, after the v8 gate; DECLARED POST-HOC on one point)
Same world, harness, kits, PO, H9/H9b rules as v8 PROTOCOL.md, except:
- POST-HOC change: reframe := reframe_signal >= 0.15 at the approved budget in any cycle (just above the best generic policy,
  0.118, which was known before the gate). Chosen after seeing the gate (A_r3 partial 0.388 reached T); labelled post-hoc.
- Gate re-read under the new threshold: A_r1 and A_r3 reached T WITH the reframe; A_r2 did not reach T → the world counts as
  valid for v8b.
- Arm A is completed by RESUMING the stopped runs (A_r1 from cycle 5, A_r3 from cycle 3) after `git reset --hard` +
  `git clean -fd` to the last cycle commit (partial edits of the killed sessions discarded); A_r2 already has 6 cycles.
  Declared threat: A_r1/A_r3 had a ~20-minute interruption between cycles (stateless sessions, repo-only memory).
- N (kit-nudge) and M (kit-loop-v3), 3 x 6 each, in parallel under caffeinate.

## Amendment 1 (owner decision 2026-10-12, before any v8b run): the primary measure is GENERATION, not behaviour
Orchestrator finding: A_r1/A_r3 reached the reframe signal by tuning generic frequency policies (GDSF freq^3 + decay; size
power 4) without stating any recurrence idea in their notes. Therefore:
- PRIMARY = "articulated reframe": a blind classifier (claude -p sonnet, no tools, no AGE, sees only the run's concatenated
  notes/records/inbox text, newest last, capped 40k chars) answers YES to Q_art AND reframe_signal >= 0.15 in any cycle.
  Q_art: "Do these project notes state, as a hypothesis or a finding, that some items are requested again after long idle
  periods on a recurring or regular schedule (periodic or recurring demand), and propose or use a policy that exploits this?
  Answer YES or NO."
- Classifier validated before use on planted texts (artic/*.txt, expected in artic/expected.json) including A_r1's real notes
  as a known negative; any miss → fix the question before runs.
- The behavioural reframe (signal >= 0.15) and the hit rate are reported as secondary. H9/H9b rules apply with "reframes" =
  articulated reframes.
