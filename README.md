# The Data Warrior’s Manuscript — rebuildable chapter scaffold

This is a **non-destructive integration package**, designed to merge into the private GitHub repository `Rla102277/the-data-warriors-manuscript`. It includes 36 provisional chapter workspaces, 20 original DOCX attachments with SHA-256 inventory, a preliminary topic crosswalk and a local Markdown assembler.

**Important:** This package is not a rewritten manuscript and has not been pushed to GitHub. Do not overwrite the existing `archive/chat-recovered/`, `PROJECT_STATE.md`, `MANUSCRIPT_ARCHITECTURE.md`, or other pre-existing repository files.

## Quick start
1. Unzip at the repository root; review merge conflicts and commit.
2. Run `python scripts/build.py --audit` to inspect readiness.
3. Map source passages and preserve author corrections.
4. Add approved chapter content in `chapter.md` with `status: approved` front matter.
5. Run `python scripts/build.py --preview` for a working Markdown assembly; `--publication` requires all chapters.
