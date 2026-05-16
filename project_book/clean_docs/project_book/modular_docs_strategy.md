# Modular Clean Docs Strategy

Project Book clean docs should stay index-driven and modular.

The business reason is simple: agents should spend context on the current decision, not on every durable note the project has ever collected.

## Strategy

1. Start with `project_book/clean_docs/index.md`.
2. Use root docs for high-level project truth.
3. Use module folders for real product or system areas.
4. Use local module indexes to route agents to focused files.
5. Use `project_book/clean_docs/relationships.md` for cross-area dependencies.
6. Split large docs before they become catch-all files.

## Preferred Structure

```text
project_book/clean_docs/
  index.md
  relationships.md
  00_project_overview.md
  01_current_state.md
  02_target_direction.md
  03_operating_rules.md
  04_next_steps.md
  05_architecture_defaults.md
  06_init_fixer_flow.md
  session_index.md
  <area>/
    index.md
    <focused_topic>.md
```

The root files should remain short and durable. Area folders carry deeper details only when those details reflect real project structure.

## Module Creation Rule

Create a module folder when at least one of these is true:

- the codebase has a real matching directory or service;
- the product has a distinct workflow area;
- a domain has separate owners, risks, inputs, or validation;
- agents repeatedly need only part of the current docs for a task.

Do not create placeholder module trees for imagined services.

## Examples

Acceptable future modules:

- `backend/` for real backend services or internal blocks.
- `frontend/` for real UI flows, design system rules, and app surfaces.
- `ai/` for real prompts, tools, model-routing, quality loops, and agent workflows.
- `data/` for real database schema, ingestion, data contracts, and migrations.
- `ops/` for real deployment, credential handling, scheduling, observability, and runbooks.
- `product/` for real user journeys, success metrics, offers, cohorts, and experiments.

For a backend with several real services, prefer:

```text
clean_docs/backend/index.md
clean_docs/backend/core/index.md
clean_docs/backend/tg-scraper/index.md
clean_docs/backend/ai-interactions/index.md
```

Use names that match the actual codebase, service, workflow, or product language.

## Fixer Behavior

The Fixer should:

- read `clean_docs/index.md` first;
- choose the smallest set of root docs and module docs needed for the task;
- put exact files in `plan.md` Required Files;
- avoid broad `clean_docs/*.md` instructions unless the task is specifically a docs inventory;
- update module indexes when it creates or moves docs.

## Netrunner Behavior

The Netrunner should:

- treat `plan.md` as the task contract;
- read the index and exact required module files;
- update only the relevant module docs when project truth changes;
- update `relationships.md` when cross-area relationships change;
- update `session_index.md` when session state changes.

## Fixer Review Behavior

During review, the Fixer should check that:

- changed docs remain discoverable from `clean_docs/index.md`;
- module docs are not duplicating root truth;
- cross-area changes are reflected in `relationships.md` when needed;
- the Netrunner did not create fake modules unrelated to real project structure.

## Handoff Behavior

The handoff should point to `clean_docs/index.md` plus the specific module docs that matter for the next action.

Do not list every clean doc in handoff unless the next action genuinely needs a full docs audit.
