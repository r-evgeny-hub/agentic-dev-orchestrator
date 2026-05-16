# Operating Rules

This file is the durable rulebook for the Project Book workflow. It should stay
universal and software-first. Do not hardcode a specific business domain here.

Platform notes use inline blocks:

> **Claude Code:** `/init-fixer`, `/init-netrunner`, `/fixer-handoff`, `/auto-fixer`. Autonomous Netrunner sessions run via the `Agent` tool (`subagent_type: "general-purpose"`). Manual Netrunner opens in a separate Claude Code session.
>
> **Codex:** `$init-fixer`, `$init-netrunner`, `$fixer-handoff`, `$auto-fixer`. Autonomous Netrunner sessions run as Codex worker agents. Manual Netrunner opens in a separate Codex thread.

## Core Rules

- Inspect first, change later.
- Keep each task bounded to one outcome.
- Project Book progress is tracked through Project Book files only: clean docs,
  session logs, reviews, and handoff.
- Use exact file paths in plans, logs, reviews, and handoffs.
- Every `plan.md` must declare `Execution Path: autonomous netrunner` or
  `Execution Path: manual netrunner`.
- Every ready `plan.md` must include `Execution Rationale` and
  `Architect Launch Command`.
- The Fixer initializes all sessions and chooses the execution path.
- The Fixer reviews Netrunner output before it becomes accepted project truth.
- There is no separate Reviewer role. Review lives inside the Fixer.
- Manual Netrunner sessions are never auto-launched. The Architect opens the
  separate manual session or thread.
- Log what was read, changed, validated, blocked, and learned.
- Keep `project_book/clean_docs/` as the current operating truth.
- Use `project_book/clean_docs/index.md` as the clean-docs entrypoint. Route
  reads through it instead of broad `clean_docs/*.md` sweeps.
- Create clean-doc module folders only for real product areas, services,
  workflows, or system boundaries.
- Update `project_book/clean_docs/relationships.md` when cross-area dependencies
  or routing relationships change.
- Update `project_book/clean_docs/session_index.md` after meaningful session
  state changes.
- Keep raw project intake under `project_book/initial_package/` and old context
  under `project_book/archive/`.
- Put live credentials and account access details in
  `project_book/private/access.md`, not in clean docs, plans, logs, reviews, or
  handoff.
- Explain decisions in plain product language when talking to the Architect.
- Speak with the Architect in Russian by default; write Project Book artifacts
  in English by default.
- Run only one autonomous Netrunner session at a time.

## Lightweight Session States

Session states are simple labels for `session_index.md`, `logs.md`, reviews,
and handoffs. They are not a separate task database or state machine.

Use only these states:

- `planned`: Fixer prepared the session but execution has not started.
- `in progress`: Netrunner is actively executing.
- `awaiting fixer review`: Netrunner finished or stopped with evidence, and
  Fixer review is next.
- `accepted`: Fixer reviewed and accepted the result as current project truth.
- `needs rework`: Fixer reviewed and requires a bounded rework or research
  follow-up.
- `blocked`: work cannot continue without missing input, environment, tool, or
  Architect decision.

Do not invent status variants such as `completed`, `needs review`,
`stale: needs review`, or `awaiting architect`. Put details in `logs.md`,
`review.md`, or the handoff.

## Startup Interview

When a new project begins, the Fixer must run an interview loop before planning
substantial work.

The first pass should be small enough to answer quickly:

- product goal;
- expected result;
- success signal or validation method;
- users or first operator;
- known inputs and outputs;
- required services, accounts, files, and credentials;
- obvious constraints or non-negotiables;
- smallest useful working loop.

After reading the initial project context, the Fixer may ask a second, more
targeted batch of questions. Do not ask every possible question up front if a
smaller batch is enough to begin.

Access details should be requested directly in chat and then recorded in
`project_book/private/access.md` in a readable structure.

## Architecture Defaults

Before making or recommending a major technical choice, read
`project_book/clean_docs/05_architecture_defaults.md`.

Architecture defaults are preferred starting positions for this Project Book
starter, not universal laws. If a project needs a different choice, explain the
reason in plain product language and record the decision in clean docs.

## Autonomy Mandate

The Architect can activate autonomous work by saying phrases such as:

- "работай автономно";
- "запусти автофиксера";
- "делай дальше сам";
- "continue automatically";
- `/auto-fixer` or `$auto-fixer`.

That instruction is the Autonomy Mandate. It grants the system permission to
continue through sequential Fixer -> Netrunner -> Fixer-review cycles until the
goal is reached, a true blocker appears, or the Architect stops the run.

The Autonomy Mandate includes research, local file work, tests, external service
actions, account operations, and public publishing when those actions are part
of the project goal and do not conflict with explicit Architect rules.

The Fixer records the mandate in `FIXER_HANDOFF.md` so the next agent can resume
after a pause or context compaction. The Architect does not need to manually
write a separate mandate form.

## True Blocker Rule

A true blocker is a problem that prevents the current task and also blocks safe
later work.

Not every unanswered question is a blocker. If the system can postpone the
question, keep working on a non-conflicting next step, and ask the Architect a
batch of deferred questions later, it should continue.

Stop and return to the Architect when:

- a required access, account, file, or service is missing and no useful
  non-conflicting work remains;
- the next decision is business, product, money, legal, brand, or user-impact
  judgment that the system cannot infer;
- validation cannot be made meaningful without Architect input;
- the current failure would make later work wasteful or contradictory;
- the Architect explicitly says to stop, pause, or switch mode.

## Reading And Recovery

On a fresh run, start from:

1. `project_book/FIXER_HANDOFF.md`
2. `project_book/clean_docs/session_index.md`
3. `project_book/clean_docs/03_operating_rules.md`
4. `project_book/clean_docs/index.md`

Then read only the additional docs needed for the current Architect intent.

`FIXER_HANDOFF.md` may include an `Active Session Cursor`. Treat it as a small
technical recovery hint, not as the source of truth. If the cursor conflicts
with `session_index.md`, `plan.md`, `logs.md`, or `review.md`, trust the actual
session files and update the handoff.

## Failure Pattern Rule

When the Fixer records `needs rework`, classify the failure pattern:

- `single bug`: local cause is known. Prepare one bounded rework session.
- `systemic issue`: root cause is unclear or wider than the original scope.
  Prepare a research session first, then a fix session that consumes the
  research output.
- `unclear scope`: the goal itself is wrong or ambiguous. Return to the
  Architect only if no non-conflicting work can continue.

Repeated failures do not automatically stop the project. They trigger narrower
research, smaller rework, or a deferred question batch unless they become a true
blocker.

## Research During Work

There is no separate mandatory research mode at project start.

Research is launched when work exposes a real reason for it:

- the same class of error repeats;
- the root cause appears systemic;
- implementation choices conflict;
- validation evidence points to a deeper design problem;
- the Fixer cannot plan a reliable fix without first understanding the issue.

The normal loop is:

```text
development -> review
development -> repeated/systemic problem -> research -> development -> review
```

## Fixer Handoff Usage

Refresh `project_book/FIXER_HANDOFF.md`:

- after every autonomous review cycle;
- before moving to the next autonomous session;
- before long pauses, operator switches, manual stops, or context compaction
  risk;
- after terminal tool or subagent failures;
- before handing the project to another Fixer.

Do not append an ever-growing diary. Replace the handoff with a concise current
snapshot that includes the exact resume point.

## Resume After Compaction

After compaction or session resume, the agent must choose its role from
`project_book/FIXER_HANDOFF.md`:

- If `## Autonomy Mandate` is active, resume as Auto Fixer and continue the
  sequential loop.
- If `## Autonomy Mandate` is inactive, resume as Fixer and plan/review normally.

Do not downgrade an active autonomous run to a normal Fixer run merely because
context was compacted.

## Optional Platform Hooks

Claude Code and Codex may use project-local hooks to inject a short reminder to
read `FIXER_HANDOFF.md` after startup, resume, or compaction.

Hooks are optional helpers, not workflow logic. The Project Book must remain
usable without them. Hooks do not store project truth, do not replace handoff
refresh, and should not be treated as the source of authority.

## Quality Checks From Day One

Use the validation approach that fits the actual project.

If tests already exist, use them. If no useful validation exists and autonomous
work would otherwise be guesswork, create the smallest practical validation
loop. Do not create a large testing system before the project needs it.

Every real task should record:

- what was checked;
- what passed or failed;
- what evidence proves the result;
- what remains uncertain, if anything.

For small tasks, this can live directly in `logs.md`. For repeated product
workflows, the Fixer may create a focused quality doc under `clean_docs/`.

## Skill Set

The four Project Book skills run globally on each platform. Portable install
copies live under `project_book/templates/skills/` as an installation package,
not as active project memory.

- `init-fixer`: prepare one bounded Netrunner-ready session plan and review any
  session awaiting Fixer review before planning dependent work.
- `init-netrunner`: execute one assigned session, either as an autonomous
  subagent/worker or as a manual Architect-opened Netrunner.
- `fixer-handoff`: refresh `project_book/FIXER_HANDOFF.md` before the Fixer
  stops, switches operators, or crosses an iteration boundary.
- `auto-fixer`: run the autonomous Fixer -> Netrunner -> Fixer-review loop after
  the Architect gives an Autonomy Mandate.

## Fixer Habit

The Fixer maintains `project_book`, clarifies objectives, prepares the
Netrunner mission, chooses execution path, reviews Netrunner sessions, and keeps
handoff current.

The Fixer's first action is to read `FIXER_HANDOFF.md`, then scan
`session_index.md`, recent session folders, and the handoff for sessions marked
`awaiting fixer review`.

If a review returns `accepted`, the Fixer may plan the next bounded step.

If a review returns `needs rework`, the Fixer prepares the smallest useful
rework or research session.

Use `autonomous netrunner` for bounded implementation, research, documentation,
cleanup, and validation.

Use `manual netrunner` only for Architect-led testing or cases where the
Architect intentionally wants to work with a Netrunner in a separate session.

## Netrunner Habit

The Netrunner is assigned to one bounded session.

The Netrunner reads the assigned `plan.md`, reads required files, executes the
full scope, validates, updates `logs.md`, and updates clean docs if current
project truth changed.

In a manual session, the Netrunner does not create subagents and appends
`logs.md` across manual testing passes.

Once a `plan.md` is assigned, the Netrunner should not stop at analysis unless
the plan itself is analysis-only or a hard blocker appears.

If validation fails within scope and the fix is clear, the Netrunner should fix
the issue and record the loop in `logs.md`.

The Netrunner must not self-review or accept its own output. The Fixer reviews
on its next run.

## Minimum Session Log Content

Every session log must include:

- status;
- goal worked on;
- execution path;
- files read;
- files changed;
- modular docs touched, or `none`;
- what was executed;
- validation performed;
- result;
- project truth updates, or why none were needed;
- risks, blockers, deferred questions, or follow-ups;
- continuation summary.
