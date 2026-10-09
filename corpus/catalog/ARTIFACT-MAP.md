# Minimal AGE project records

Use the project's current version-control and document conventions. These are **information contracts**, not a mandatory directory structure or data model.

## Core records

1. **Attractor charter:** Current approved direction, capabilities, invariants, tradeoffs, negative scope, decision authority, version history.
2. **Experiment protocol:** Decision at stake, observation, claim, strongest rival, mechanism, prediction, falsifier, baseline/oracle, scope, freeze record, stop conditions.
3. **Evidence record:** What was run/observed, by whom/what, with which versions and limitations; pointers to raw outputs and failed runs.
4. **Verdict:** One of four sanctioned values, scope, supporting evidence, caveats, implementation status, failed/fired falsifier.
5. **Evolution decision:** Concrete next action or stop, alternatives, link to attractor, approval, reversal conditions.
6. **Immersion transfer note (optional):** External observation, proposed structural analogy, breakdown risks, untested target claim.
7. **Portfolio index (optional):** Active, retired, blocked, superseded, and dependent claims.

## Source of truth

Use immutable Git commits/links or equivalent versioned identifiers for experiments and decisions. Do not overwrite previous results to improve a narrative. Keep a lightweight index readable by a new agent without an external database.

## Record creation policy

Create records only when the corresponding activity occurs. Routine delivery need not create an experiment record. Small teams should start with a handful of Markdown documents and repository-native test artifacts. Do not build AGE-specific storage or UI until a measured need exists.

## Reader contract

A new agent must be able to answer: what is the current attractor, which claims are live, what was rejected and why, what has been decided, who authorized changes, and what is the next highest-impact unknown?
