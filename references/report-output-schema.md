# Reader-facing report contract

## Required sections

1. **Scope and identity:** artifact, version, source/file, publication date, verification date, and exclusions.
2. **Method:** claim selection, atomization, source strategy, support/refutation searches, access limits, sampling, expert consultation, and current-information cutoff.
3. **Status legend:** define all four labels and state that Unable to confirm is not false.
4. **Executive findings:** material findings, status composition, scope-only count, and limitations.
5. **Claim table:** one row per atomic claim.
6. **Evidence ledger:** exact source, passage, support/counterevidence, citation fit, limitations, and repair for material claims.
7. **Citation/reference findings:** identity, retrieval, version, substantive support, quotations, retractions, and missing/misleading citations.
8. **Publication-type findings:** apply the relevant module and distinguish factual failures from methodological limitations or interpretive overreach.
9. **Repairs and escalations:** precise correction, narrowing, qualification, replacement source, removal, or human review.
10. **Unresolved questions:** inaccessible sources, conflicting evidence, unavailable data, missing expertise, and what would resolve the issue.

## Claim table

| ID | Location | Claim | Type | Scope | Materiality | Status | Confidence | Coverage | Key reason |
|---|---|---|---|---|---|---|---|---|---|

Scope-only claims should show `not_fact_checkable` and their scope reason instead of a status.

## Style

Write plainly and specifically. Keep the original claim visible. Link or identify inspectable evidence. Do not use “proved” when evidence only supports or contradicts. Do not call an author dishonest without separate evidence of intent. Do not use confidence language to conceal missing evidence.

## Structured output

When JSON is requested, use [evidence-ledger-schema.json](evidence-ledger-schema.json). Provide a Markdown report alongside JSON unless JSON-only is explicitly requested.
