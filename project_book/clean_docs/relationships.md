# Relationship Map

This file records how durable Project Book areas connect.

Keep it short. It is a routing map, not a replacement for module documentation.

## Current Starter Relationships

| Area | Connects To | Relationship |
| --- | --- | --- |
| `project_book/clean_docs/` | `project_book/templates/` | Clean docs define current truth; templates turn that truth into repeatable session artifacts. |
| `project_book/clean_docs/` | global Project Book skills | Skills read clean docs to plan, execute, review, and hand off bounded sessions. |
| `project_book/session_logs/` | `project_book/clean_docs/session_index.md` | Session logs are detailed history; the session index is the current routing view. |
| `project_book/session_logs/` | Fixer review | Finished Netrunner work becomes accepted truth only after Fixer review records acceptance. |
| `$auto-fixer` | `project_book/FIXER_HANDOFF.md` | Automatic mode refreshes handoff and `Compression Snapshot` after review cycles so work can resume after context compaction. |
| `project_book/initial_package/` | `project_book/clean_docs/` | Raw intake starts in `initial_package/`; distilled durable truth moves into clean docs. |
| `project_book/archive/` | active docs | Archive keeps stale context out of active truth. |

## Future Project Relationship Pattern

When a real project exists, add only the relationships that help agents choose the right docs:

| Area | Connects To | Relationship |
| --- | --- | --- |
| `backend` | `data` | Example: owns writes, reads, migrations, or product APIs. |
| `frontend` | `backend` | Example: calls product APIs and displays user-facing workflows. |
| `ai` | `backend` / `tools` | Example: performs interpretation through scoped product tools. |
| `ops` | all runtime areas | Example: deployment, secrets, scheduled jobs, logs, and rollback notes. |

Replace examples with real project areas when they exist.

## Update Rule

Update this file when:

- a new module directory is created;
- a service boundary changes;
- one module starts depending on another;
- a session changes how agents should route between docs.

Do not add implementation detail here. Put details in the relevant module file.
