# HC Technology Selection Framework

STATUS: BOOTSTRAP_BASELINE
FRONT: I

## Principle

HC selects technologies from requirements and capabilities. It does not build a
tool tournament and does not treat popularity, installation or successful demos
as ownership decisions.

## Lifecycle

CANDIDATE
→ RESEARCHED
→ SELECTED_FOR_POC
→ IMPLEMENTED
→ VERIFIED
→ ACTIVE_OWNER

Alternative outcomes:

- REJECTED
- DEFERRED
- SUPERSEDED
- RETIRED

Each transition requires explicit evidence.

## Selection flow

1. Define capability requirement.
2. Define architectural constraints.
3. Research market and technical landscape.
4. Eliminate candidates that fail hard requirements.
5. Record unresolved material uncertainty.
6. Write an ADR when a choice becomes architectural.
7. Run a targeted PoC only where uncertainty justifies execution.
8. Verify the PoC against acceptance criteria.
9. Adopt behind a replaceable adapter.
10. Reassess through Technology Watch.

## Evaluation dimensions

At minimum:

- architectural fit;
- capability coverage;
- isolation;
- reliability;
- checkpoint/resume;
- multi-executor coordination;
- observability;
- security;
- credential model;
- permission model;
- operability;
- Windows/WSL/Linux compatibility as relevant;
- API/protocol stability;
- licensing;
- project maturity;
- community/maintainer health;
- upgrade risk;
- replaceability;
- total operational cost.

## PoC doctrine

A PoC exists to answer a material unresolved question.

A PoC must specify:

- hypothesis;
- scope;
- acceptance criteria;
- prohibited side effects;
- evidence;
- rollback;
- terminal decision.

Successful execution alone does not imply adoption.

## ADR doctrine

Architecture Decision Records should capture:

- context;
- requirements;
- options considered;
- decision;
- rationale;
- evidence;
- risks;
- rejected alternatives;
- reversibility;
- reassessment trigger.

## Technology Watch

Technology Watch is read-only intelligence.

It may propose:

- reassessment;
- new research;
- security response;
- migration study.

It may not automatically:

- install;
- upgrade;
- replace;
- promote;
- retire

a technology owner.

## Candidate isolation

Non-selected candidates must remain isolated from canonical authority and
production ownership.

Adapters must prevent a candidate-specific API from becoming an accidental
system contract.
