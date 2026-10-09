# Hypothesis Spike — protocol contract

Write this **before** building the substantive experiment or seeing the outcome. It should be comprehensible to a skeptical agent not involved in framing the thesis.

## Required sections

### Decision at stake
Which concrete investment, design, or practice would change depending on the result? State the default decision without new evidence.

### Observation and uncertainty
What happened or remains unresolved? Separate facts from interpretation.

### Hypothesis
Make a bounded, potentially false claim. Avoid aspirations disguised as hypotheses.

### Strongest rival
Describe a plausible alternative as fairly as its strongest advocate would. Include a conventional baseline when relevant.

### Mechanism and assumptions
Why might the claim hold, and what must be true for that to occur?

### Differentiating predictions
Describe what the candidate and rival should produce under the same meaningful conditions.

### Falsifier and decision thresholds
Identify the result that would cause rejection, and what counts as meaningful support. State the scope and fairness conditions. Qualitative thresholds are acceptable when appropriate and justified.

### Independent checking
Specify oracle, external references, holdout, baseline, or adversarial evaluation. Identify shared-author risks.

### Minimal experiment
State what will be built or observed and what will deliberately *not* be built. Include stop and safety conditions.

### Freeze and dependencies
Record the approved/frozen evaluation version and any prerequisites whose failure would block the experiment.

## Contract tests

A good protocol lets a second evaluator distinguish SUPPORTED, REJECTED, INCONCLUSIVE and INVALID without negotiating new criteria after observing results. It specifies at least one possible failure of the favored claim. Its outcome could change a real decision.
