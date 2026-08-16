# Research corpus and design provenance

## Contents

- Professional standards
- Role and workflow texts
- Publication integrity
- Computational verification
- Skill architecture
- Adopted principles

## Professional standards

- [IFCN Code of Principles](https://ifcncodeofprinciples.poynter.org/the-commitments): nonpartisanship, source transparency, methodology, corrections.
- [SPJ Code of Ethics](https://www.spj.org/spj-code-of-ethics/): verification, original sources, context, accountability, correction.
- [Reuters standards](https://reutersagency.com/about/standards-values/): independent verification of AI-generated facts and sources.
- [AP News Values](https://www.ap.org/about/news-values-and-principles/telling-the-story/): attribution, data integrity, context, visible corrections.
- [UNESCO Module 5](https://www.unesco.org/sites/default/files/module_5.pdf): selecting claims, finding evidence, evaluating truthfulness.
- [FactCheck.org process](https://www.factcheck.org/our-process/): line-by-line checking, primary evidence, claimant response, corrections.
- [AFP How We Work](https://factcheck.afp.com/How-we-work): cross-checking, context, archives, no denial-only proof.
- [Full Fact uncertainty guidance](https://fullfact.org/media/uploads/en-communicating-uncertainty.pdf): insufficient evidence differs from false.

## Role and workflow texts

- [The New Yorker, “Checkpoints”](https://www.newyorker.com/magazine/2009/02/09/checkpoints).
- [The Fact Checker’s Bible](https://www.penguinrandomhouse.com/books/169512/the-fact-checkers-bible-by-sarah-harrison-smith/).
- [The Chicago Guide to Fact-Checking](https://press.uchicago.edu/ucp/books/book/chicago/C/bo194938501.html).
- [KSJ fact-checking process](https://ksjhandbook.org/fact-checking-science-journalism-how-to-make-sure-your-stories-are-true/the-fact-checking-process/).
- [TiJ editorial process](https://thetijproject.ca/guide/the-editorial-process/).
- [Verification Handbook 2](https://verificationhandbook.com/downloads/verification.handbook.2.pdf).

## Publication integrity

- [APA Journal Article Reporting Standards](https://www.apa.org/pubs/journals/int/submit).
- [EQUATOR Network](https://www.equator-network.org/reporting-guidelines/).
- [ICMJE accountability guidance](https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html).
- [COPE Retraction Guidelines](https://publicationethics.org/sites/default/files/retraction-guidelines-cope.pdf).

## Computational verification

- [FEVER](https://fever.ai/dataset/fever.html): claim-level support, refute, and insufficient-information framing.
- [SciFact](https://arxiv.org/abs/2004.14974): scientific claim verification, evidence retrieval, and rationales.

## Skill architecture

- [Codex skill-creator](https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/skill-creator/SKILL.md): concise metadata, progressive disclosure, references, scripts, validation, and forward testing.
- [Hermes skills](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md): Agent Skills-compatible directories and progressive disclosure.
- [Claude Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): filesystem packages with SKILL.md, references, scripts, and surface-specific runtime constraints.

## Adopted principles

1. Evidence must be inspectable and traceable.
2. The claim as written is the object of checking.
3. Context, timeframe, scope, and qualifiers are part of the claim.
4. Primary and independent evidence are preferred.
5. Support and refutation searches are required for material claims.
6. Uncertainty is a result, not a failure.
7. Corrections are part of the system.
8. Status, confidence, materiality, access, and source quality are separate.
9. Reporting standards do not prove truth or validity.
10. AI must not claim work, access, or certainty it does not possess.
