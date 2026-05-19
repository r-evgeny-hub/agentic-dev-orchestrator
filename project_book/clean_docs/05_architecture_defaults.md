# Architecture Defaults

This file defines preferred starting positions for building AI-assisted products.

Use it before choosing cloud platform, backend stack, database, AI runtime, service boundaries, storage, secrets, scheduling, logging, MCP/server integrations, or deployment direction.

These defaults are not universal laws. If a project needs a different choice, explain the reason in plain product language.

## Core Direction

Build the useful product loop first.

Do not build a full platform before the product has a small working path.

A project usually has two goals:

- product value: the thing works and produces a useful result
- learning value: the Architect understands how to build better AI systems

First prove the working path. Put learning into short explanations, dry runs, and small experiments.

## Preferred Defaults

| Area | Preferred Default |
| --- | --- |
| Cloud platform | GCP |
| Backend/runtime hosting | Cloud Run |
| Batch jobs | Cloud Run Jobs |
| Scheduled work | Cloud Scheduler for deterministic recurring work |
| Secrets | Secret Manager or environment variables |
| Generated files and artifacts | Cloud Storage or object storage |
| Logs | Simple run logs first; Cloud Logging on GCP |
| Database | GCP-native database as the initial source of truth |
| Database selection | Start with the simplest GCP fit: Firestore for document/state data, Cloud SQL when relational SQL is clearly needed, and BigQuery for analytics |
| Backend language | Go for new backend services by default |
| Frontend | Vite + React + TypeScript + Tailwind + shadcn/ui + Lottie |
| Frontend hosting | Vercel is acceptable short-term; GCP can be used when one-cloud simplicity matters |
| AI runtime | Codex-first for multi-step agentic work |
| Codex control layer | Codex SDK + Codex App Server as a private control/runtime layer |
| Quality | Small golden set and manual quality notes from day one |

## Language Defaults

Use Go for new backend services by default.

Deviate from Go when the domain ecosystem strongly favors another language, especially when mature libraries, protocol support, or existing working code make another language lower-risk.

In that case, document the reason for the deviation.

## Service Boundaries

Separate business responsibilities clearly before splitting deployment units.

If two parts of a product must live independently, be reused independently, or connect to different future products, they can be separate services from the start.

If a large AI-heavy part is still uncertain, keep it as a splittable monolith first: one deployable unit with clear internal blocks.

Internal blocks should be named by responsibility, such as:

- primary analysis or enrichment
- core domain operations
- user interaction or chat

Do not turn every conceptual block into a separate microservice on day one.

Good early architecture should make future extraction possible without forcing it too early.

## Infrastructure Principles

Choose infrastructure that is understandable to both a human and an AI assistant.

Good infrastructure makes these things clear:

- where the data lives
- where the code runs
- where the logs are
- where the secrets are
- how to repeat a run

Before choosing a service, check:

1. Can the data be exported?
2. Do the skills transfer to future projects?

Prefer transferable surfaces such as:

- GCP-native managed databases with clear export paths
- Docker / Cloud Run
- object storage
- clear logs

## Risk First

If one risk can kill the product, test that risk before building the full skeleton.

Common early risks in AI products:

- can the required input be collected reliably?
- can the AI workflow produce a useful result?
- can the project run outside a local machine?
- can the AI layer avoid a fragile provider-specific process?

## System Layers

Use system layers as a map, not as a requirement to build everything immediately.

The useful map is:

1. triggers
2. data
3. backend logic
4. AI task execution
5. tools
6. knowledge
7. memory
8. quality checks
9. observability
10. user interface

A good project knows which layers exist, which are deferred, and why.

## Storage Boundaries

| Thing | Preferred Place |
| --- | --- |
| Current project truth | `project_book/clean_docs/` |
| Task history | `project_book/session_logs/` |
| Secrets | Secret Manager or environment variables |
| Product working data | Database |
| Large generated files | Object storage |
| Old source material | `project_book/initial_package/` or `legacy/` |

Rules:

- The database should not become a dump for large files.
- `clean_docs` should not become a diary.
- Archives and old context should not clutter the repository root.

## Deterministic Work

Do not use AI orchestration for work that should be deterministic.

Use normal backend code, cron jobs, queues, and database state for predictable operations such as scheduled sync, polling, status updates, and simple data movement.

Use Codex or another AI runtime where the work requires interpretation, synthesis, tool use, file-aware reasoning, or multi-step judgment.

## AI Runtime Principles

For multi-step AI work, start with one strong Codex-controlled run.

Do not begin by splitting the workflow into many small specialist agents.

Do not design the MVP around many Responses API microsteps.

Split later only after repeated real failures show a stable boundary.

Codex App Server is a private control layer. Do not expose it directly to public frontend users.

The frontend should call the backend. The backend may control Codex.

Agent tools should be product-oriented where possible:

- `get user profile`, not `raw database tool`
- `save product record`, not `database write`
- `upload artifact`, not `storage tool`
- `create download link`, not `file operation`

## MCP And Tool Boundaries

When an AI workflow needs to read product data or perform product actions, prefer an MCP/server-tool boundary instead of giving the AI broad direct access to the database or internal systems.

The tool layer should expose product-level actions with explicit schemas and scope.

Examples:

- `get_current_user_messages`, not unrestricted database access
- `search_workspace_sources`, not raw access to all stored files
- `save_analysis_result`, not arbitrary writes
- `create_download_link`, not direct storage access

For multi-user products, the MCP server or backend tool layer must authenticate the current user or workspace and return only data within that scope.

Do not rely on prompts alone to prevent cross-user data leakage. Put access limits in code, database policy, or the MCP/server-tool boundary.

Use MCP as a contract boundary: the AI can call only the tools that exist, in the formats those tools define, with the permissions those tools enforce.

## User Data Boundaries

Do not give an AI workflow broad access to every user's data.

Put user scoping into the backend, database policies, and MCP/server tool boundary.

A user-scoped tool should only return data for the current user or current workspace.

## Historical And Live Data

For data-ingestion products, separate historical backfill from ongoing live collection.

The system should know:

- what has already been collected
- what is still being processed
- where live collection starts
- when downstream analysis is allowed to consume the data

Do not let downstream AI analysis treat partially processed data as complete.

## Run Identity And Quality

Every meaningful run should have a stable identifier:

- `run_id`
- product object id, such as `object_id`
- clear log path or log record

From day one, keep a simple quality loop:

- a few concrete examples
- expected output notes
- manual review notes
- common failure notes
- prompt or code version when useful

Start with simple run logs. Add heavier observability only after the first real loop works.

## Reproducibility Check

A product is not proven only because it works for the builder's own account.

For integrations with personal accounts, APIs, credentials, or external platforms, run at least one end-to-end check with another user or another account before treating the integration as reusable.
