# Sbooks — Shaden Enterprises Operations Platform

## What This Project Is
Beverage distribution operations platform for a beer/soda wholesale business (Shaden Enterprises). Manages daily operations across salespersons, stock managers, business managers, and the owner.

## Tech Stack
- **Backend:** FastAPI + SQLModel + PostgreSQL (Neon, async)
- **Mobile:** React Native
- **Admin/Dashboard:** FastHTML
- **Hosting/Jobs:** Modal
- **Auth:** JWT + RBAC (role-based access control)

## Project Structure
```
sbooks/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── database.py           # Async PostgreSQL connection (Neon)
│   ├── core/                 # Config, security, dependencies
│   │   └── __init__.py
│   ├── models/               # SQLModel table classes (41 tables, 8 clusters)
│   │   └── __init__.py
│   └── routers/              # API endpoint modules
│       └── __init__.py
├── migrations/               # Alembic migration scaffold (env.py, script.py.mako, versions/)
├── alembic.ini               # Alembic configuration
├── .env                      # Environment variables (DO NOT COMMIT)
├── requirements.txt          # Python dependencies
├── PROGRESS.md               # Project progress tracker & session log
├── SESSION_PRACTICES.md      # Industry standard tracking/cleanup reference
├── se_ffstyle.ipynb          # Project tracking overview notebook
└── venv/                     # Virtual environment (DO NOT COMMIT)
```

## Data Model
41 tables across 8 clusters:
1. **People & Access** — users, roles, permissions
2. **Products & Inventory** — brands, categories, SKUs, stock
3. **Vehicles & Customers** — vehicles, customers, routes/territories
4. **Daily Operations** — deliveries, route management
5. **Financial** — transactions, payments, reporting
6. **Orders** — order lifecycle
7. **Stock Audit Trail** — audit, reconciliation
8. **Targets & Notifications** — KPIs, alerts

MVP scope: 25 tables (Phase 1), 16 deferred (Phase 2).

Full data model specification is in: `../problem_statement_data_model_redesign_clean_v1_dup1.ipynb`

## 4 Roles
- **Salesperson** — field sales, order entry, customer management
- **Stock Manager** — inventory, warehouse, stock audits
- **Business Manager** — operations oversight, reporting
- **Owner** — full access, financials, targets

## Working Style
- **Ask before implementing** — don't jump to writing code or running commands. Present the approach first and let the user decide whether to execute it themselves or have Claude do it. Sometimes the user wants to learn, not just get output.
- **Never run side-effecting actions unless explicitly told to** — this includes `git commit`, `git push`, `git amend`, force-pushes/resets, closing/labeling/commenting on GitHub issues or PRs, merging, deploying, and adding `closes #X`/`fixes #X` to commit or PR text (those auto-close issues on merge). Asking for a *commit message* is not asking for a commit. Asking to *finish a task* is not asking to close its issue. Provide the command or text; let the user run it. Authorization for one action never extends to adjacent actions.

## Code Quality Standard
- **Always default to the latest, non-deprecated, production-ready API** — this is what goes in the code
- **Listing options is fine** — when multiple approaches exist, you may explain the alternatives for context, but always clearly label the best-in-class version and use that in any code you write
- **Never suggest a deprecated pattern without flagging it** — if existing project code uses a deprecated API, call it out immediately
- **Check library version before suggesting patterns** — e.g., Pydantic V2 uses `model_config = SettingsConfigDict(...)` not class-based `Config`

## Coding Preferences
- Use async/await throughout (async database sessions, async endpoints)
- SQLModel for all ORM models (not raw SQLAlchemy)
- Pydantic schemas via SQLModel (shared model/schema where possible)
- Type hints everywhere
- Keep routers thin — business logic in service layers when complexity warrants it
- Use dependency injection for database sessions and auth

## Current State
- Phase 3 (Architecture & Design) in progress — Phase 3.1 (Core Wiring) almost done; Alembic install + scaffold complete; configuration + empty baseline migration remain
- `.gitignore` done (`venv/`, `.env`, `__pycache__/`, `*.pyc`); venv untracked from git ✅
- `requirements.txt` pinned via `pip freeze` — GitHub issue #10 CLOSED ✅
- `README.md` populated — project overview, features, setup guides (new contributor + owner + production) ✅
- `app/core/config.py` written ✅ — loads `DATABASE_URL` and `JWT_SECRET` via pydantic-settings; `field_validator` normalizes Neon URL for asyncpg (scheme→`postgresql+asyncpg`, `sslmode`→`ssl`, drop `channel_binding`) using `urllib.parse`
- `app/database.py` written ✅ — async engine, session factory, `get_session` dependency (GitHub issue #11 CLOSED)
- `app/main.py` written ✅ — `lifespan` with startup `SELECT 1` Neon health check + `engine.dispose()` on shutdown; `app = FastAPI(lifespan=lifespan)` (commit `a5db6e2`; GitHub issue #12 still OPEN until manually closed — `closes #12` in the commit message only auto-closes on merge to default)
- `SESSION_PRACTICES.md` — added principle "Diff Before Committing Auto-Generated Files" (Session 9)
- Auto-created issues #1–#7 deleted; labels + milestone kept; issue #8 closed
- GitHub labels (chore, core, auth, models, sprint-1) and milestone (Sprint 1 — People & Access) in place
- `.env` populated — `DATABASE_URL` (Neon) and `JWT_SECRET` added ✅
- Neon end-to-end verified ✅ (lifespan `SELECT 1` succeeded against Neon)
- Alembic installed ✅; scaffold created via `alembic init -t async migrations` ✅ (folder is `migrations/`, not `alembic/` — paths in any docs/scripts must use `migrations/`)
- **Next:** (1) Configure `alembic.ini` and `migrations/env.py` — pull `DATABASE_URL` from `app.core.config.settings`, set `target_metadata = SQLModel.metadata`. (2) Create + apply empty baseline migration: `alembic revision -m "initial"` then `alembic upgrade head`. Then Phase 3.2 (SQLModel classes for Sprint 1 — People & Access)
- See `PROGRESS.md` for detailed status and session log

## Development Plan
9 sprints planned — Sprint 1 (People & Access) is next. See `PROGRESS.md` for full sprint breakdown.
