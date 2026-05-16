# Project Initialization

Use this template only when starting a new project.

The goal is to interview the Architect, catch the important product and
architecture choices early, collect required access details, and then write the
distilled result into `project_book/clean_docs/`.

Do not keep the raw interview as active project truth.

## Goal

Turn a broad idea into:

- product value;
- learning value;
- inputs;
- outputs;
- users or first operator;
- success signal;
- first working loop;
- main risks;
- required access;
- initial architecture direction.

## First Question Batch

Ask a minimal set first so the project can start without turning the interview
into bureaucracy:

1. What should this product do in one sentence?
2. Who will use it first?
3. What input data does it receive?
4. What result should it produce?
5. How will we know the result is good?
6. What is the smallest useful working loop?
7. What external accounts, APIs, services, credentials, files, or datasets does
   it depend on?
8. What could block all later work if it fails?
9. What should the first bounded Netrunner session prove?

## Second Question Batch

After the Fixer reads the initial context, it may ask a second, sharper batch
only for missing information that materially improves planning:

- which parts must work live or repeatedly;
- which parts must work historically from existing data;
- what user, workspace, account, or data boundary matters;
- what should be deterministic code, data, scheduling, or queue work;
- what genuinely needs AI judgment, tool use, or multi-step synthesis;
- which architecture defaults apply or should be changed;
- what can be deferred safely.

## Access Collection

Ask for required access directly in chat.

Record real values in:

```text
project_book/private/access.md
```

Use a readable structure so both the Architect and agents can open the file and
understand what is available:

```markdown
## <Service Or Account>

- URL:
- Login:
- Password:
- API key / token:
- Notes:
- Used for:
```

Do not duplicate access values in clean docs, session logs, reviews, or handoff.

## Defaults To Consider

Before making a technical recommendation, compare the project against
`project_book/clean_docs/05_architecture_defaults.md`.

Use architecture defaults as starting positions, not universal laws.

## After The Interview

Write the distilled result into:

- `project_book/clean_docs/00_project_overview.md`
- `project_book/clean_docs/01_current_state.md`
- `project_book/clean_docs/02_target_direction.md`
- `project_book/clean_docs/04_next_steps.md`

Then create the first bounded session plan under `project_book/session_logs/`.

The first session should prove one small useful loop, not design the whole
platform.

Every first session plan must declare `Execution Path: autonomous netrunner` or
`Execution Path: manual netrunner`.

Every first session plan must also include `Execution Rationale` and
`Architect Launch Command`.
