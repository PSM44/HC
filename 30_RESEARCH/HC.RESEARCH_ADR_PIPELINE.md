# HC Technology Research / ADR Pipeline

STATUS: IMPLEMENTATION_BASELINE
FRONT: P12
VERSION: v0.1

## Flow

CAPABILITY_NEED
→ RESEARCH_RECORD
→ HARD_REQUIREMENT_FILTER
→ MATERIAL_UNCERTAINTY
→ ADR_OR_DEFER
→ TARGETED_POC_IF_REQUIRED
→ VERIFICATION
→ LIFECYCLE_DECISION
→ TECHNOLOGY_WATCH

Research does not itself promote technology ownership.

## Research record

Each material candidate investigation records:

- technology ID;
- capability need;
- sources;
- requirements;
- architecture fit;
- security/trust observations;
- operability;
- maturity;
- licensing;
- cost considerations;
- unresolved uncertainty;
- recommended next action.

## ADR

An ADR is required when the decision materially affects architecture,
ownership, interfaces, durability, security or replacement strategy.

ADR decisions remain reversible unless explicitly classified otherwise.

## PoC gate

PoC is used only for unresolved material uncertainty.

PoC acceptance criteria must be written before execution.

Successful execution is evidence, not automatic adoption.

## Lifecycle authority

Technology Registry transitions require evidence.

`ACTIVE_OWNER` requires explicit architectural decision and VERIFIED status.

Technology Watch remains read-only intelligence.

Canonical ADR template:

`30_RESEARCH/adr/ADR.TEMPLATE.md`

Canonical research-record schema:

`30_RESEARCH/schemas/technology-research-record.schema.json`
