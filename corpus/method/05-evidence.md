# 05 — Evidence, verdicts, and experimental integrity

AGE distinguishes a working artifact from a supported reason to adopt it.

## Two ledgers

**Implementation health:** Can the artifact execute its intended test scenario without known defects? Typical values: healthy, failing, blocked, unknown.

**Hypothesis verdict:** What do the experiment's claims and falsifiers say? Exactly one of:

- **SUPPORTED:** Predeclared support criterion was met, within recorded scope. This is provisional evidence, not proof of universal truth.
- **REJECTED:** Predeclared reject criterion or falsifier was met, within scope.
- **INCONCLUSIVE:** The protocol was valid but evidence did not settle the claim.
- **INVALID:** The test, oracle, contamination, or execution violated requirements badly enough that its result cannot answer the claim.

A green implementation can accompany a rejected economic or architectural hypothesis. A broken harness should produce INVALID, not a dramatic REJECTED.

## Evidence hierarchy

Prefer independent domain reference models or external oracles; strong baseline comparisons; meaningful property/state-machine tests; mutation tests showing falsifiers really detect defects; deterministic replay; preregistered benchmarks. Expert judgment and embodied/subjective observation remain useful when labeled and applied to claims that legitimately require them.

## Integrity rules

- Preserve the original protocol and the actual outcome. New conditions require a new version.
- Never fill missing evidence with generated explanatory prose.
- Don't use the candidate implementation as its sole oracle.
- Check whether a test can detect the very failure it claims to find.
- Record agent shared-author risks, biased task sampling, hidden cost, unsuitable proxies, contamination, and external-validity limits.
- Count dependencies, glue, maintenance, generated-file churn, security burden, operator effort, and failure recovery where material.
- Declare what has **not** been tested.

## Human evaluation

Not every quality has a computable oracle. For creative, somatic, or ethical objectives, specify observation protocols and honest subjectivity. Do not pretend that a rubric score is a physiological measurement or a value judgment is a technical theorem.

## Reproducibility

Evidence should point to immutable or versioned records, tooling versions, baseline conditions, and a way to repeat or inspect the decision. Narrative summaries are views over evidence, not substitutes for it.
