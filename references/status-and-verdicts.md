# Status, confidence, and roll-up rubric

## Contents

- Status semantics
- Scope-only claims
- Confidence and coverage
- Materiality and risk
- Document roll-up

## Status semantics

Status answers: “What does the available evidence establish about this claim as written?” It is not a probability, a measure of honesty, or a general judgment about the document.

### Strongly confirming

Use only when direct, inspectable, high-quality evidence supports the claim’s scope, timeframe, definitions, quantities, attribution, quotation, context, and causal strength; the evidence is primary or authoritative; independent corroboration is present when needed or a unique authoritative record is sufficient; and no material counterevidence, qualification, citation mismatch, or calculation problem remains.

### Confirming

Use when adequate direct evidence supports the claim as written and no material contradiction exists, but a meaningful nonfatal limitation remains, such as limited corroboration, a narrower source, a moderate caveat, incomplete access, or a less-than-ideal source. Do not use it for evidence that merely suggests or repeats the claim.

### Unable to confirm

Use when a proportionate search cannot establish truth or falsity. Record one subtype:

- `no_adequate_evidence_found`
- `source_inaccessible`
- `claim_underspecified`
- `not_currently_falsifiable`
- `materially_conflicting_evidence`
- `evidence_too_indirect_or_narrow`
- `evidence_stale_or_incomplete`

This is not a false rating.

### Inaccurate

Use when a material element is contradicted, materially misstated, unsupported by the cited source, presented with false context, quoted or attributed incorrectly, causally overstated, generalized beyond the evidence, or materially stale. Record one inaccuracy type. Do not infer intent.

## Scope-only claims

Opinions, values, predictions, pure hypotheticals, and genuinely non-falsifiable propositions receive:

- `claim_scope: not_fact_checkable`
- `scope_reason`
- `reason`
- `source_access_level: not_applicable`
- `evidence_coverage: not_applicable`

They must not receive `status` or `confidence`. Factual premises embedded in them are separate claims and should be checked normally.

## Confidence

Confidence is confidence in the assigned status:

- **High:** direct, inspectable, high-quality evidence with little material uncertainty.
- **Medium:** supported status with meaningful limitations, partial coverage, source conflict, or interpretation.
- **Low:** provisional status with indirect evidence, poor definition, limited access, or material disagreement.

Do not increase confidence because many derivative sources repeat one origin.

## Evidence coverage and access

`evidence_coverage` values:

- `full_text_or_full_record`
- `substantive_excerpt`
- `abstract_or_summary_only`
- `metadata_only`
- `snippet_only`
- `no_inspectable_evidence`
- `not_applicable`

`source_access_level` values:

- `direct_full_access`
- `partial_access`
- `indirect_access`
- `inaccessible`
- `not_applicable`

Strongly confirming cannot use snippet, metadata, abstract-only, no-evidence, or not-applicable coverage.

## Materiality and risk

Materiality: `critical`, `high`, `medium`, or `low`.

Risk: `critical`, `high`, `medium`, or `low`.

Critical/high claims include safety, legality, serious allegations, scientific validity, public decisions, thesis, headline, executive summary, major result, causal interpretation, or recommendations.

## Document roll-up

Prefer claim-level findings and a status composition. If one overall status is required:

1. `Inaccurate` if any material or high-risk claim is Inaccurate.
2. Otherwise `Unable to confirm` if any material claim is Unable to confirm.
3. Otherwise `Confirming` if all material claims are Confirming or Strongly confirming and at least one is Confirming.
4. `Strongly confirming` only if every material fact-checkable claim is Strongly confirming and no material uncertainty remains.

Exclude scope-only claims from the status composition, but report their count and scope reasons. Set `mixed_findings: true` when fact-checkable claim statuses differ.

## Minimum reason

Use:

> The claim is **[status]** because **[specific evidence]** matches or conflicts with **[precise claim element]**; **[limitation/counterevidence]**; therefore confidence is **[level]**.

For scope-only claims, explain why the proposition is outside factual verification and identify any factual premises checked separately.
