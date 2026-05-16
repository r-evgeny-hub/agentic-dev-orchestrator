# Project Book Skills Rebuild Reference

Use this file when a new environment does not already have the required Project
Book skills installed globally.

Canonical portable copies live here:

```text
project_book/templates/skills/
  claude/
    init-fixer/
    init-netrunner/
    fixer-handoff/
    auto-fixer/
  codex/
    init-fixer/
    init-netrunner/
    fixer-handoff/
    auto-fixer/
```

These folders are an installation package, not active project-local skills.

## Required Skills

Install all four:

- `init-fixer`
- `init-netrunner`
- `fixer-handoff`
- `auto-fixer`

## Install Targets

Claude Code:

```text
~/.claude/skills/<skill-name>/SKILL.md
```

Codex:

```text
$CODEX_HOME/skills/<skill-name>/SKILL.md
```

Codex skill folders may also include:

```text
agents/openai.yaml
```

## Shared Concepts

All four skills follow these rules:

- speak with the Architect in Russian unless asked otherwise;
- write Project Book artifacts in English unless the task requires another
  language;
- treat `project_book/clean_docs/` as current project truth;
- request access details in chat and record real values in
  `project_book/private/access.md`;
- route clean-doc reads through `project_book/clean_docs/index.md`;
- use exact file paths;
- use exactly these statuses:
  - `planned`
  - `in progress`
  - `awaiting fixer review`
  - `accepted`
  - `needs rework`
  - `blocked`
- run one autonomous Netrunner at a time;
- refresh `FIXER_HANDOFF.md` after every autonomous review cycle.

## Autonomy Mandate

The Architect activates autonomous work by saying phrases such as:

- "работай автономно";
- "запусти автофиксера";
- "делай дальше сам";
- `/auto-fixer`;
- `$auto-fixer`;
- "continue automatically".

This instruction is the Autonomy Mandate. The Fixer records it in
`FIXER_HANDOFF.md`; the Architect does not manually fill a separate form.

When active, the system continues through sequential Fixer -> Netrunner ->
Fixer-review cycles until the goal is reached or a true blocker appears.

## True Blocker

A true blocker is a problem that prevents the current task and also blocks safe
later work.

If a question can be deferred and non-conflicting work can continue, record the
question and keep moving.

## Skill Responsibilities

### `init-fixer`

- Run the startup interview when project context is incomplete.
- Maintain Project Book truth.
- Review sessions marked `awaiting fixer review`.
- Prepare one bounded Netrunner-ready `plan.md`.
- Decide autonomous vs manual execution path.
- Update handoff when stopping or crossing an iteration boundary.

### `init-netrunner`

- Execute one assigned session.
- Validate results.
- Update `logs.md`.
- Update clean docs if current truth changed.
- Set session status to `awaiting fixer review`, `needs rework`, or `blocked`.
- Never self-review.

### `fixer-handoff`

- Refresh `FIXER_HANDOFF.md`.
- Preserve Autonomy Mandate state, current objective, next action, and exact
  next command.
- Optionally include Active Session Cursor or Compression Snapshot as recovery
  hints, not as sources of project truth.
- Avoid duplicating large docs or access values.

### `auto-fixer`

- Run sequential autonomous cycles after the Architect gives an Autonomy Mandate.
- Launch one autonomous Netrunner at a time.
- Review results before dependent work.
- Launch research sessions when repeated or systemic problems appear.
- Stop only for a true blocker or Architect interruption.

## Optional Claude Code Compaction Helper

Claude Code uses `.claude/settings.json`:

```json
{
  "autoCompactEnabled": true,
  "autoCompactWindow": 400000
}
```

This is a Claude Code platform setting for when compaction happens. It is not a
Project Book planning rule and must not be used as a rule for splitting tasks.

The hook layer may inject Project Book resume reminders after compaction or
resume. Hooks are optional helpers, not workflow logic. Project Book must remain
usable from `FIXER_HANDOFF.md` and the session files without hook support.

## Optional Codex Compaction Helper

Codex uses:

```text
.codex/hooks.json
project_book/tools/project_book_resume_hook.py
```

The hooks may inject resume reminders on session start/resume and on
continuation-like user prompts. Handoff refresh at iteration boundaries remains
the recovery mechanism.

## Installation Check

After installation, verify these files exist:

```text
<global-skill-root>/init-fixer/SKILL.md
<global-skill-root>/init-netrunner/SKILL.md
<global-skill-root>/fixer-handoff/SKILL.md
<global-skill-root>/auto-fixer/SKILL.md
```

Then run:

```text
Run /init-fixer.
```

or:

```text
Activate skill $init-fixer.
```
