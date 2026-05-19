# Agentic Dev Orchestrator

Agentic Dev Orchestrator is a lightweight autonomous framework for AI-assisted
development. It turns product intent into scoped Project Book sessions, runs
sequential Fixer / Netrunner work in Codex or Claude Code, reviews evidence, and
preserves project memory across sessions.

The internal mechanics still use the Fixer / Netrunner model:

- **Fixer** clarifies intent, plans bounded work, reviews evidence, and updates
  project truth.
- **Netrunner** executes one scoped implementation or research session.
- **Project Book** keeps durable memory, logs, decisions, and handoff state.

It works on both Claude Code and Codex. The same Project Book files, templates,
and role skills are used on both platforms; only skill invocation syntax,
subagent mechanism, and manual-session container differ. It can also serve as a
workflow layer around SDK-based agent runners.

## Why This Exists

AI coding agents are powerful, but long-running development work breaks down
when context is scattered across chats, terminals, partial plans, and
half-remembered decisions.

Agentic Dev Orchestrator gives the agent team a durable working memory:

- what the project is trying to achieve;
- what is true right now;
- what changed in each bounded work session;
- what evidence proves the work is done;
- where the next operator should resume.

The goal is not to create process for its own sake. The goal is to make AI
development work more inspectable, recoverable, and useful for business/product
outcomes.

## What This Is

Agentic Dev Orchestrator is an operating system for AI development work:

```text
Architect intent
  -> Fixer clarifies and plans
  -> Netrunner executes one bounded session
  -> Fixer reviews evidence
  -> Project Book records current truth
  -> next session or autonomous continuation
```

The four role skills are:

- **`init-fixer`**: planning, context control, review, and next-step routing.
- **`init-netrunner`**: execution of one bounded session.
- **`fixer-handoff`**: current-state recovery snapshot.
- **`auto-fixer`**: sequential autonomous Fixer -> Netrunner -> Fixer-review loop.

## Who It Is For

Use this if you want AI agents to work on projects that need more than one
prompt:

- product prototypes;
- internal tools;
- marketing automation;
- AI agent workflows;
- research-to-build loops;
- technical migrations;
- projects where future agents need to understand what already happened.

It is especially useful when the human owner thinks in outcomes, metrics, and
tradeoffs, while the agent handles implementation details.

## Quick Start

1. Use this repository as a template or copy this folder into the project
   workspace.
2. Pick your platform and read its entry point:
   - **Claude Code:** read [`CLAUDE.md`](CLAUDE.md).
   - **Codex:** read [`AGENTS.md`](AGENTS.md).
3. Install the four role skills globally. Follow [`INSTALL_SKILLS.md`](INSTALL_SKILLS.md).
4. Describe the project to the Fixer.
5. Let the Fixer run the startup interview, collect access details, write clean
   project truth, and create the first bounded Netrunner session.

## What You Get

- A normalized `project_book/` structure.
- Clean docs for current state, target direction, operating rules, next steps,
  architecture defaults, relationships, and session index.
- Session logs with `plan.md`, `logs.md`, and `review.md`.
- A current `FIXER_HANDOFF.md` recovery snapshot.
- Installable role skills for Claude Code and Codex.
- Optional compaction/resume hooks.
- A private access file pattern that keeps secrets out of public docs.

## Key Mechanics

- **Startup interview**: the Fixer must ask missing questions before substantial
  work begins. It asks a minimal first batch, then a sharper second batch only
  when useful.
- **Access collection**: required logins, passwords, tokens, service links, and
  account notes are requested directly in chat and recorded in
  `project_book/private/access.md`.
- **Acceptance gate**: Netrunner output becomes project truth only after Fixer
  review records `accepted`.
- **Sequential execution**: one autonomous Netrunner at a time.
- **Autonomy Mandate**: when the Architect says "работай автономно", "запусти
  автофиксера", "делай дальше сам", `/auto-fixer`, `$auto-fixer`, or equivalent,
  the system continues autonomously until the goal is reached or a true blocker
  appears.
- **True blocker rule**: if a question can be deferred and non-conflicting work
  can continue, the system continues and asks later in a batch.
- **Research on demand**: no separate research phase is required at the start.
  Research is launched when repeated or systemic problems appear during work.
- **Handoff protection**: `FIXER_HANDOFF.md` keeps the current resume point so
  agents do not need to rediscover the project after pauses or compaction.

## Folder Tour

```text
README.md
CLAUDE.md
AGENTS.md
INSTALL_SKILLS.md
.claude/settings.json
.codex/
  config.toml
  hooks.json
project_book/
  AGENTS.md
  README.md
  VERSION.md
  FIXER_HANDOFF.md
  archive/
  fixer_logs/
  initial_package/
  private/
    access.md
  session_logs/
  clean_docs/
    index.md
    00_project_overview.md
    01_current_state.md
    02_target_direction.md
    03_operating_rules.md
    04_next_steps.md
    05_architecture_defaults.md
    06_init_fixer_flow.md
    relationships.md
    session_index.md
    project_book/
      index.md
      automatic_mode.md
      modular_docs_strategy.md
  templates/
    plan.md
    logs.md
    fixer_review.md
    autonomy_mandate_note.md
    project_initialization.md
    project_book_skills_rebuild.md
    skills/
      codex/
      claude/
  tools/
    project_book_resume_hook.py
```

## Platform Differences

| Aspect | Claude Code | Codex |
| --- | --- | --- |
| Skill invocation | `/init-fixer`, `/init-netrunner`, `/fixer-handoff`, `/auto-fixer` | `$init-fixer`, `$init-netrunner`, `$fixer-handoff`, `$auto-fixer` |
| Skills install path | `~/.claude/skills/<name>/SKILL.md` | `$CODEX_HOME/skills/<name>/SKILL.md` |
| Autonomous Netrunner | `Agent` tool, `subagent_type: "general-purpose"` | Codex worker agent |
| Manual session container | Separate Claude Code session | Separate Codex thread |
| Compaction handling | Optional compact-resume reminder plus handoff | Optional `.codex/hooks.json` reminder plus handoff |

## Where Things Live

- Current project truth: `project_book/clean_docs/`
- Access details: `project_book/private/access.md`
- Per-session work evidence: `project_book/session_logs/<date>/<task>/logs.md`
- Fixer acceptance/rework decision: `review.md` in the session folder
- Current resume point: `project_book/FIXER_HANDOFF.md`
- Skill install package: `project_book/templates/skills/`
- Optional hook resume helper: `project_book/tools/project_book_resume_hook.py`

## Resume After Compaction

After context compaction, the correct role is determined by
`project_book/FIXER_HANDOFF.md`:

- Autonomy Mandate active: resume as Auto Fixer and continue sequentially.
- Autonomy Mandate inactive: resume as Fixer and ask/plan normally.

The platform hooks only inject reminders. They do not store project truth, do
not control workflow logic, and are not required for Project Book to work.

## License

MIT. Use it, adapt it, fork it, and make it fit your own AI project workflow.
