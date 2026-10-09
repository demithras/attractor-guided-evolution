# Experiment evidence and verdict — record contract

Create after execution; do not rewrite the frozen protocol. Refer back to the exact protocol version.

## Required sections

### What was actually done
Run identifiers, tools, environment, dataset/task sample, deviations, agent or human roles, and raw output references.

### Evidence for and against
Show the strongest supportive result and strongest counterexample, using their actual recorded scope. Say which expected tests or observations are missing.

### Integrity audit
Assess independence of oracle, baseline fairness, contamination, missing data, protocol changes, statistical/sampling limitations, and any known evaluator weaknesses. Note whether the falsifier itself was tested against a planted or known defect when appropriate.

### Implementation status
Report whether the prototype worked as implemented. Never collapse this into the hypothesis verdict.

### Hypothesis verdict
Use exactly one of SUPPORTED, REJECTED, INCONCLUSIVE, INVALID. Explain the frozen criterion applied. If the protocol changed materially, mark this run INVALID for the frozen claim and create a new protocol version.

### Limits and next decision
What does this not prove? Which dependent work is blocked? What next action could be warranted, without pretending that a verdict automatically authorizes production edits?

## Integrity check

Can a reviewer trace each claimed observation to evidence? Is a post-hoc narrower claim explicitly labeled as new? Does the record honestly preserve failed and inconclusive runs?
