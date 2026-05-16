# Project Book Module

This module documents the Project Book starter itself: clean docs, templates,
skills, session logs, access file, and handoff flow.

## Owns

- Project Book operating rules.
- Modular clean-docs strategy.
- Session planning, logging, review, and handoff conventions.
- Automatic Project Book work mode.
- Starter templates for future projects.
- Portable install package for the four required Project Book skills.
- Fixer-owned review stage after Netrunner execution.

## Read For

Read this module when a task changes:

- `project_book/AGENTS.md`
- `project_book/README.md`
- `project_book/templates/`
- `project_book/private/access.md` structure
- global Project Book skills:
  - `$init-fixer` / `/init-fixer`
  - `$init-netrunner` / `/init-netrunner`
  - `$auto-fixer` / `/auto-fixer`
  - `$fixer-handoff` / `/fixer-handoff`
- clean-docs structure or routing rules
- session lifecycle rules

## Module Files

- `project_book/clean_docs/project_book/modular_docs_strategy.md`: index-driven
  modular clean-doc strategy.
- `project_book/clean_docs/project_book/automatic_mode.md`: autonomous
  Fixer/Netrunner/Fixer-review loop, true blockers, and compression handoff rules.

## Dependencies

- Reads from root clean docs for current project truth.
- Uses `project_book/clean_docs/relationships.md` to keep cross-area routing visible.
- Uses `project_book/session_logs/` and `project_book/clean_docs/session_index.md`
  for session state.
- Uses `project_book/private/access.md` only when a task needs access details.

## Out Of Scope

- Product-specific backend, frontend, data, ops, or AI implementation details.
- Historical archive details unless a plan explicitly asks for them.
- Large copied transcripts; summarize durable decisions instead.
