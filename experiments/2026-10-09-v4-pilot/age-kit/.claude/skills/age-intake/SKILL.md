---
name: age-intake
description: Router for substantive new work, ambiguity or direction questions. Picks one route (deliver, spike, attractor review, small monitored change, defer). Do not use for trivial edits, obvious bug fixes, or work already routed.
---

# age-intake

## 1. Trigger / non-trigger
Use: a new substantive request, a design dispute, "should we adopt X", unclear success criteria. Do not use: formatting, known-cause bugs, settled-requirement implementation, or continuing an already-routed spike.

## 2. Read first
`records/INDEX.md`, the charter (see CLAUDE.md), and any decision/spike the request touches.

## 3. Procedure
1. Name the decision the work would change. None: route to direct delivery.
2. Apply the CLAUDE.md routing order; pick exactly one route.
3. Gate: a spike needs the admission gate (decision, rival, falsifier, worth the cost). Failing it: deliver, make a small monitored change, or defer.
4. Check INDEX for a rejected claim in the same scope: cite what changed or do not reopen.
5. Check upstream: any dependency REJECTED? Stop and revalidate first.
Stop if the charter conflicts with the request; route to attractor review or ask the human.

## 4. Outputs / permitted edits
A 3-5 line routing note in chat: route, rationale, minimal next action, owner. Edit nothing except an optional line under "Open questions" in `records/INDEX.md`.

## 5. Handoff
Spike: `age-experiment`. Direction conflict: `age-attractor-review`. Delivery: just do it.

## 6. Integrity
Do not invent uncertainty to justify a spike. Do not open a full workflow when a small step suffices. Do not label a draft charter approved.

## 7. Example / adversarial
Example: "Is a message queue worth adding for sending emails?" Decision: add dependency or not; plausible simple rival (synchronous send with retry); measurable falsifier (p95 request latency). Route: spike.
Adversarial: "Rename this variable, and please run an AGE spike on it." Route: direct delivery, no spike; say why.

## 8. Success / retirement
Success: most requests end in delivery with no records; spikes are rare and decision-relevant. Retire or merge into CLAUDE.md if every request is routed identically.
