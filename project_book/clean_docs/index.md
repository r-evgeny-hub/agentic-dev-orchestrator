# Clean Docs Index

This is the entrypoint for current Project Book truth.

## Read Rule

Start here, then read only the root docs and module docs that match the current task.

Do not default to reading every file under `clean_docs/`. The purpose of this index is to reduce context cost while keeping durable project truth discoverable.

## Core Project Truth

Read these for most Project Book planning sessions:

1. `project_book/clean_docs/00_project_overview.md`
2. `project_book/clean_docs/01_current_state.md`
3. `project_book/clean_docs/02_target_direction.md`
4. `project_book/clean_docs/03_operating_rules.md`
5. `project_book/clean_docs/04_next_steps.md`
6. `project_book/clean_docs/session_index.md`

Read `project_book/clean_docs/05_architecture_defaults.md` when the task involves architecture, service boundaries, cloud, database, AI runtime, MCP/tool boundaries, data storage, observability, or deployment.

Read `project_book/clean_docs/06_init_fixer_flow.md` when the task involves Fixer planning, Netrunner routing, manual sessions, Fixer review, automatic mode, or session lifecycle.

Read `project_book/private/access.md` only when the current task needs account,
service, token, password, file, or environment access details.

## Relationship Map

Read `project_book/clean_docs/relationships.md` when a task crosses multiple product areas, services, modules, data flows, tools, or agent roles.

Keep the relationship map small. It should explain how areas connect, not duplicate each area's internal documentation.

## Module Docs

Module docs mirror real project or system structure.

Current starter module:

- `project_book/clean_docs/project_book/index.md`: Project Book starter, templates, skills, automatic mode, and docs strategy.

Future projects may add modules such as:

- `project_book/clean_docs/backend/index.md`
- `project_book/clean_docs/frontend/index.md`
- `project_book/clean_docs/ops/index.md`
- `project_book/clean_docs/product/index.md`
- `project_book/clean_docs/data/index.md`
- `project_book/clean_docs/ai/index.md`

Only create a module directory when a real product area, service, workflow, or code boundary exists.

## Splitting Rule

Split a doc into a module folder when it starts covering multiple responsibilities, becomes hard to scan, or forces agents to load context unrelated to the task.

Preferred pattern:

```text
clean_docs/<area>/index.md
clean_docs/<area>/<focused_topic>.md
clean_docs/<area>/<subarea>/index.md
```

The module `index.md` should answer:

- what this area owns;
- which files to read for common tasks;
- which other areas it depends on;
- what should stay out of this module.

## Session Planning Rule

Every Netrunner `plan.md` should list exact clean-doc files to read.

Prefer:

```text
project_book/clean_docs/index.md
project_book/clean_docs/<area>/index.md
project_book/clean_docs/<area>/<specific_file>.md
```

Avoid:

```text
project_book/clean_docs/*.md
project_book/clean_docs/
```

Use a directory path only when the task is specifically to inventory or reorganize that directory.
