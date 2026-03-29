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

## Coding Preferences
- Use async/await throughout (async database sessions, async endpoints)
- SQLModel for all ORM models (not raw SQLAlchemy)
- Pydantic schemas via SQLModel (shared model/schema where possible)
- Type hints everywhere
- Keep routers thin — business logic in service layers when complexity warrants it
- Use dependency injection for database sessions and auth

## Current State
- Phase 3 (Architecture & Design) in progress — Phase 3.0 (Project Setup) partially done
- `.gitignore` done (`venv/`, `.env`); venv untracked from git ✅
- `requirements.txt` still empty — GitHub issue #10 open
- Core plumbing (`database.py`, `main.py`, `config.py`) still empty — needs GitHub issue created
- Auto-created issues #1–#7 deleted; labels + milestone kept; issue #8 closed
- GitHub labels (chore, core, auth, models, sprint-1) and milestone (Sprint 1 — People & Access) in place
- **Next:** Create core plumbing issue, populate requirements.txt (#10), wire up plumbing, then Phase 3.1
- See `PROGRESS.md` for detailed status and session log

## Development Plan
9 sprints planned — Sprint 1 (People & Access) is next. See `PROGRESS.md` for full sprint breakdown.
