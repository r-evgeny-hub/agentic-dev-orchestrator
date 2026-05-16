# Codex Project Memory

This workspace uses the Project Book workflow. The agent-facing entry point is
`project_book/AGENTS.md`; read it first.

This template is unified across Codex and Claude Code. Platform-specific syntax
inside the docs appears in `> **Codex:** ...` and `> **Claude Code:** ...`
blocks. On Codex, follow the Codex blocks.

## Read Order

1. `project_book/AGENTS.md`
2. `project_book/README.md`
3. `project_book/FIXER_HANDOFF.md`
4. `project_book/clean_docs/03_operating_rules.md`
5. `project_book/clean_docs/index.md`
6. `project_book/clean_docs/session_index.md`

Conditional reads only when current intent requires them:

- `project_book/clean_docs/00_project_overview.md`
- `project_book/clean_docs/01_current_state.md`
- `project_book/clean_docs/02_target_direction.md`
- `project_book/clean_docs/04_next_steps.md`
- `project_book/clean_docs/05_architecture_defaults.md`
- `project_book/clean_docs/06_init_fixer_flow.md`
- Module docs named by `clean_docs/index.md`
- `project_book/clean_docs/relationships.md`

If `project_book/FIXER_HANDOFF.md` contains an `Active Session Cursor`, treat
it as a small recovery hint only. Actual session files remain the source of
truth.

## Role Skills

This workflow expects four global Codex skills:

- `$init-fixer`: plan one bounded Netrunner session and review awaiting sessions.
- `$init-netrunner`: execute one bounded session.
- `$fixer-handoff`: refresh current resume state.
- `$auto-fixer`: continue sequential autonomous work after the Architect gives an
  Autonomy Mandate.

If any are missing, install them from `project_book/templates/skills/codex/` or
rebuild them from `project_book/templates/project_book_skills_rebuild.md`.

## Defaults

- Speak with the Architect in Russian.
- Write Project Book artifacts in English.
- Run one autonomous Netrunner at a time.
- Ask startup questions before substantial work begins.
- Request required access directly in chat and record it in
  `project_book/private/access.md`.
- When the Architect says to work autonomously, continue until the goal is
  reached or a true blocker appears.
- Refresh `FIXER_HANDOFF.md` after every autonomous review cycle and before any
  pause, operator switch, or context-risk boundary.

## Optional Codex Compaction Helper

This template includes `.codex/hooks.json` as an optional helper.

The hooks may inject Project Book resume context on session start/resume and
when the Architect submits a continuation-like prompt. They are reminders only;
the workflow must still work from `project_book/FIXER_HANDOFF.md` and the
session files without hook support.

The primary protection is `project_book/FIXER_HANDOFF.md`, refreshed at
iteration boundaries.
