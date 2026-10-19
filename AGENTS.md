# Cross-tool collaboration contract

Applies to ChatGPT, Cursor, Codex, Claude, and other assistants.

## Session startup
Read README.md, PROJECT_STATE.md, DECISIONS.md, and MANUSCRIPT_ARCHITECTURE.md before substantive edits. Read relevant chapter/source files before changing them.

## Editorial invariants
- The human practitioner is the Data Warrior; AI augments rather than replaces judgment.
- Five Rings (Earth, Water, Fire, Wind, Void) are Musashi's structure. People, Tools, and Practice are explicitly modern extensions.
- The Living Scroll houses and supports a challenge throughout its lifecycle; it is not merely a document generator.
- Preserve named Council roles: Strategist, Architect, Engineer, Guardian, Examiner, Sensei.
- The Battle Map includes objectives, terrain, dependencies, actions, risks, decisions, and proof.
- Distinguish sourced historical quotations from modern interpretations. Never invent quotations.
- Keep the book readable independently of its companion software.

## Editing discipline
- Do not overwrite or delete earlier manuscript material without reviewing and preserving it.
- Prefer small, coherent commits with descriptive messages.
- Mark speculative decisions as proposals; do not silently promote them to approved.
- When changing architecture, update DECISIONS.md and MANUSCRIPT_ARCHITECTURE.md.
- After each session, update PROJECT_STATE.md: what changed, why, unresolved issues, and exact next step.
- Never commit credentials, private correspondence, or unlicensed third-party content.

## Response handoff
Summarize changed paths, decisions, unresolved questions, and commit hash. Another assistant should be able to resume from repository files alone.
