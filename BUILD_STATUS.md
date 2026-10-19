# Build status — 2026-10-19

## Completed locally
- 20 original DOCX files preserved byte-for-byte in `archive/originals/`.
- Complete SHA-256 and word-count inventory in `planning/SOURCE_INVENTORY.json`.
- 4,750 source sections indexed in `planning/SOURCE_SECTIONS.jsonl`, retaining filename, heading, paragraph range and original paragraph text.
- 36 chapter workspaces, each with `SOURCE_CANDIDATES.md`, machine-readable `source-candidates.json`, and an explicitly **unapproved** `chapter.md` with up to two source excerpts selected by a keyword heuristic.
- 77K-word source-reconstruction assembly in `build/source-reconstruction.md`. **Not an author-approved rewritten book**. May repeat material and include source inconsistencies.
- 120.9K-word paragraph-text extraction of the longest original manuscript in `archive/extracted/THE_WAY_OF_THE_DATA_WARRIOR_full_text.md`.
- Scripts: `scripts/reconcile.py` regenerates the source index and candidates; `scripts/assemble_sources.py` regenerates source-based chapter drafts and assembly; `scripts/build.py` audits and builds only approved chapters.

## Not yet completed
- Recovered December/June Claude text is in the existing private GitHub repository under `archive/chat-recovered/`, **not copied into this package**. Preserve it when merging. Those chapters have not been crosswalked at paragraph level.
- No chapter has been human-reviewed or approved. There is no honest basis to label the 36 chapters publication-ready.
- The quote attributions, research claims, personal anecdotes and cross-chapter continuity have not been fact-checked.
- GitHub push is not confirmed; merge this package into the private repo without overwriting existing paths.

## How to run
`python scripts/reconcile.py`
`python scripts/assemble_sources.py`
`python scripts/build.py --audit`

For a true book: review candidates, reconcile chat and DOCX originals, promote approved chapter prose, run continuity and attribution checks, then build publication editions.
