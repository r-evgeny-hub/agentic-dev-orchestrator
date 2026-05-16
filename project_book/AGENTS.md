# AGENTS.md

This folder is the portable Project Book starter for AI-assisted, software-first
projects. It works on both Codex and Claude Code; platforms differ only in skill
syntax, subagent mechanism, and manual-session container.

> **Claude Code:** subagents run via the `Agent` tool (`subagent_type: "general-purpose"`); manual Netrunner opens in a separate Claude Code session; skill syntax `/init-fixer`, `/init-netrunner`, `/fixer-handoff`, `/auto-fixer`.
>
> **Codex:** subagents run as Codex worker agents; manual Netrunner opens in a separate Codex thread; skill syntax `$init-fixer`, `$init-netrunner`, `$fixer-handoff`, `$auto-fixer`.

## First Rule

Keep Project Book operating files inside `project_book/`. Do not create extra
root-level process docs unless the Architect explicitly asks for them.

Project Book tracks its own progress through clean docs, session logs, reviews,
and handoff. Do not add a separate progress-management layer to Project Book.

Project Book skills run globally. Portable install copies may live under
`project_book/templates/skills/`, but they are an installation package, not
active project memory.

## Project Initialization

When starting a new project, use `templates/project_initialization.md` for the
initial interview.

The Fixer must ask missing questions before substantial work begins. It should
start with a minimal question batch, then ask a second sharper batch only if the
project context requires it.

Required logins, passwords, tokens, service links, and account notes are
requested directly in chat and recorded in `project_book/private/access.md`.

After the interview, distill answers into `clean_docs/`. Do not keep the raw
interview itself as active project truth.

Use `clean_docs/index.md` as the clean-docs entrypoint. Create module folders
only for real product or system areas. See
`clean_docs/project_book/modular_docs_strategy.md`.

## Architecture Defaults

Before making or recommending a major technical choice, read
`clean_docs/05_architecture_defaults.md`.

Major technical choices include cloud platform, hosting, database, backend
language, AI runtime, service boundaries, storage, credentials handling,
scheduling, logging, MCP/server integrations, and deployment strategy.

Use architecture defaults as preferred starting positions, not universal laws.
If recommending a different choice, explain the reason in plain product language.

## Agent Roles

- **Architect:** human owner of business intent, product judgment, priorities,
  and final decision.
- **Fixer:** planning, context-control, review, handoff, and project-memory agent.
- **Netrunner:** execution agent for one bounded `plan.md`.
- **Autonomous Netrunner:** platform subagent/worker for bounded work that can be
  finished without step-by-step Architect input.
- **Manual Netrunner:** separate Architect-opened session/thread without
  subagents, used for intentional interactive testing or small repair batches.
- **Auto Fixer:** sequential autonomous controller for Fixer -> Netrunner ->
  Fixer-review cycles after the Architect gives an Autonomy Mandate.

The Fixer reviews every session marked `awaiting fixer review` before dependent
work. There is no separate Reviewer role.

## Read Order

On a fresh run, read:

1. `FIXER_HANDOFF.md`
2. `README.md`
3. `clean_docs/03_operating_rules.md`
4. `clean_docs/index.md`
5. `clean_docs/session_index.md`

Conditional reads:

- `clean_docs/00_project_overview.md`, `01_current_state.md`,
  `02_target_direction.md`, or `04_next_steps.md` for product strategy or
  roadmap work.
- `clean_docs/05_architecture_defaults.md` for technical decisions.
- `clean_docs/06_init_fixer_flow.md` for session routing or execution path.
- Module docs named by `clean_docs/index.md` when their area is in scope.
- `clean_docs/relationships.md` when work crosses areas, modules, services,
  tools, or product roles.
- `project_book/private/access.md` only when the current task needs access
  details.

If `FIXER_HANDOFF.md` contains an `Active Session Cursor`, treat it as a small
recovery hint only. Actual session files remain the source of truth.

## Operating Rules

- Speak with the Architect in Russian by default.
- Write Project Book artifacts in English by default.
- Keep work bounded to one outcome.
- Run one autonomous Netrunner at a time.
- Use exact file paths.
- Tell Netrunner agents exactly which files to read first.
- Route clean-doc reads through `clean_docs/index.md` and relevant module indexes.
- Every session `plan.md` must declare `Execution Path: autonomous netrunner` or
  `Execution Path: manual netrunner`.
- Every ready session `plan.md` must include `Execution Rationale` and
  `Architect Launch Command`.
- Fixer initializes both autonomous and manual sessions.
- Fixer must tell the Architect the recommended executor, reason, session path,
  and exact command to say next.
- Fixer must review sessions marked `awaiting fixer review` before dependent
  work.
- Netrunner output becomes current project truth only after Fixer review records
  `accepted`.
- Manual sessions are never auto-launched.
- Auto Mode runs when the Architect gives an Autonomy Mandate in chat or platform
  command.
- Auto Mode continues sequentially until the project goal is reached or a true
  blocker appears.
- Questions that do not block later work should be deferred and batched.
- Research sessions are launched when repeated or systemic problems appear
  during work, not as a mandatory upfront phase.
- Refresh `FIXER_HANDOFF.md` after every autonomous review cycle and before
  pauses, manual sessions, operator switches, or context compaction risk.
- After context compaction or session resume, choose the role from
  `FIXER_HANDOFF.md`: active Autonomy Mandate means Auto Fixer; inactive means
  Fixer.
- Update `clean_docs/` when current project truth changes.
- Update module indexes and `relationships.md` when routing or cross-area
  dependencies change.
- Update `clean_docs/session_index.md` when session state changes.
- Keep raw project intake under `initial_package/` and stale context under
  `archive/`.
- Keep access values in `private/access.md`; do not duplicate them into active
  operating docs.

## Session Contract

Every Netrunner session lives here:

```text
session_logs/<YYYY-MM-DD>/<task_slug>/
  plan.md
  logs.md
  review.md
```

The `plan.md` is the Fixer-to-Netrunner contract. The `logs.md` is the
Netrunner-to-Fixer execution record. The `review.md` is the Fixer acceptance,
rework, or blocker decision.

Every ready `plan.md` must include:

```text
Execution Path: autonomous netrunner / manual netrunner
Execution Rationale: why this executor is correct
Architect Launch Command: the exact command the Architect should say next
```

Valid statuses:

- `planned`
- `in progress`
- `awaiting fixer review`
- `accepted`
- `needs rework`
- `blocked`

## Required Global Skills

- `init-fixer`
- `init-netrunner`
- `fixer-handoff`
- `auto-fixer`

If any skills are missing in a new environment, install from
`templates/skills/` or rebuild from `templates/project_book_skills_rebuild.md`.

## Auto Mode

Auto Mode is activated by the Architect's instruction, not by a manually edited
form.

When active, the system records the Autonomy Mandate in `FIXER_HANDOFF.md`,
runs one autonomous Netrunner at a time, reviews each result, refreshes handoff,
and continues until the goal is reached or a true blocker appears.

## Optional Hook Resume Layer

Platform hooks may call `project_book/tools/project_book_resume_hook.py`.

The helper reads `FIXER_HANDOFF.md` and injects only a short role reminder:
continue as Auto Fixer when the Autonomy Mandate is active; otherwise resume as
Fixer. It does not store project truth, does not control workflow logic, and
does not replace handoff refresh.
