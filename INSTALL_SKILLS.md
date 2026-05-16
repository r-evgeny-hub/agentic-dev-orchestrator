# Installing the Project Book Skills

This template expects four global skills to exist on your machine. They run
globally and are reused across Project Book projects.

Install-ready portable copies live in:

```text
project_book/templates/skills/
  claude/
  codex/
```

The rebuild reference is:

```text
project_book/templates/project_book_skills_rebuild.md
```

## Pick Your Platform

- **Claude Code:** install from `project_book/templates/skills/claude/`.
- **Codex:** install from `project_book/templates/skills/codex/`.

## Claude Code Installation

Install path:

```text
~/.claude/skills/<skill-name>/SKILL.md
```

Skill folders:

```text
~/.claude/skills/init-fixer/SKILL.md
~/.claude/skills/init-netrunner/SKILL.md
~/.claude/skills/fixer-handoff/SKILL.md
~/.claude/skills/auto-fixer/SKILL.md
```

Copy each matching folder from:

```text
project_book/templates/skills/claude/<skill-name>/
```

Verify:

```text
Run /init-fixer.
```

## Codex Installation

Install path:

```text
$CODEX_HOME/skills/<skill-name>/SKILL.md
```

Skill folders:

```text
$CODEX_HOME/skills/init-fixer/
$CODEX_HOME/skills/init-netrunner/
$CODEX_HOME/skills/fixer-handoff/
$CODEX_HOME/skills/auto-fixer/
```

Copy each matching folder from:

```text
project_book/templates/skills/codex/<skill-name>/
```

If your Codex version expects UI metadata, keep the included
`agents/openai.yaml` files.

Verify:

```text
Activate skill $init-fixer.
```

## After Installation

1. Open `project_book/FIXER_HANDOFF.md` and confirm it points to a fresh project
   with no active Netrunner sessions.
2. Describe the project to the Fixer.
3. Let the Fixer ask startup questions, collect access details, update clean
   docs, and create the first bounded Netrunner session.

## Optional Claude Code Resume Helper

This template ships `.claude/settings.json` with optional hooks that may remind
Claude Code to read `FIXER_HANDOFF.md` after compaction or resume. It is a
helper only; the handoff and session files remain the durable recovery
mechanism.

## Optional Codex Compaction Helper

This template includes optional project-local Codex hooks:

```text
.codex/config.toml
.codex/hooks.json
project_book/tools/project_book_resume_hook.py
```

The hooks add resume reminders on session start/resume and on continuation-like
user prompts. They are helpers only; Project Book must still work from
`FIXER_HANDOFF.md` and the session files without hooks.

Refresh `FIXER_HANDOFF.md` after every autonomous review cycle and before
pauses or operator switches.

## Troubleshooting

- **Skill is not recognized.** Ensure the file is exactly `SKILL.md` and the
  YAML frontmatter is at the top with no leading blank lines.
- **Auto Mode does not continue.** Confirm the Architect gave an Autonomy
  Mandate in chat or command form, and confirm `FIXER_HANDOFF.md` records it.
- **The Fixer keeps re-reading all docs.** Refresh `FIXER_HANDOFF.md` with a
  tighter `Read First` list and exact next action.
- **A task feels too broad.** The Fixer should prepare one concrete bounded
  session with exact files, validation, and a stop condition.
