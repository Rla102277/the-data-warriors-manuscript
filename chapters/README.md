# Rebuildable chapter workspaces

All 36 chapter folders are scaffolded across eight provisional books, using the chapter architecture in `MANUSCRIPT_ARCHITECTURE.md`. Each folder has a README describing source reconciliation and editorial approval. These are not finished chapters.

## Source preservation
- `archive/chat-recovered/`: recovered conversations and reconstructed drafts, already committed.
- `archive/originals/`: original Word manuscript files, still pending import.
- `chapters/<book>/<number>-<slug>/`: per-chapter workspace, organized by subject rather than old chapter number.

## Expected files per completed chapter
- `sources/manifest.md` — exact source and passage mapping
- `author/` — verbatim author-provided stories and corrections
- `research/` — historical Musashi quote verification and evidence
- `drafts/` — alternatives and preserved revisions
- `chapter.md` — selected and approved chapter text
- `sword-drills.md` — exercises
- `DECISIONS.md` — editorial decision trail

## Publication rule
Do not label a chapter approved until source reconciliation, factual verification, and editorial review are complete. A full publication build must fail if required chapters are missing. Preserve original files unchanged and never overwrite recovered history.

## Current import status
The 36 chapter READMEs are committed. The locally generated source-rebuild package (20 DOCX originals, automated excerpt drafts, source indexes, build scripts) has **not** been uploaded to GitHub yet. Do not confuse folder scaffolding with a full manuscript merge.
