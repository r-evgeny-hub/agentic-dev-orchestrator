# Project Book Template Version

## Current

- Version: 1.0.0
- Codename: unified-autonomous
- Date: 2026-05-16
- Compatibility:
  - Claude Code skills 1.0.x
  - Codex skills 1.0.x

## Principles

- One Project Book system for Claude Code and Codex.
- Universal and software-first; no hardcoded business domain.
- Sequential autonomous execution; no parallel Netrunners by default.
- Autonomy is activated by the Architect's instruction in chat or command form.
- No separate manual Auto Mode form is required.
- True blockers stop work; deferrable questions are batched while safe work
  continues.
- Project Book progress is tracked through Project Book files only.
- Access values live in `project_book/private/access.md`.
- Platform hooks are optional helpers; handoff refresh and session files are the
  durable recovery mechanism.

## Changes From Earlier Drafts

- Unified Codex and Claude Code into one starter.
- Replaced the manual autonomy form with Autonomy Mandate recorded by the
  Fixer in `FIXER_HANDOFF.md`.
- Added `project_book/private/access.md` for readable access storage.
- Standardized statuses:
  - `planned`
  - `in progress`
  - `awaiting fixer review`
  - `accepted`
  - `needs rework`
  - `blocked`
- Kept `templates/fixer_review.md` as the single review template.
- Added portable physical skill copies under `templates/skills/`.
- Removed Project Book references to repository-management workflows.
- Preserved `FIXER_HANDOFF.md` as the continuity mechanism. Active Session
  Cursor and Compression Snapshot are optional recovery hints inside handoff.
- Added a cross-platform hook helper that can remind the agent to read handoff
  after compaction or resume.
- Aligned the workflow around lightweight Project Book files, optional resume
  hints, and sequential autonomous execution.
- Added explicit startup interview and access collection rules.

## Migration Note

Existing projects should not be migrated automatically. For an existing Project
Book, the Architect should decide whether to adopt this template and then copy
over only the relevant operating rules, templates, and skills.
