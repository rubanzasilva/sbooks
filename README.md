# Sbooks - Shaden Enterprises Operations Platform

A beverage distribution operations platform for a beer/soda wholesale business. Manages daily operations across salespersons, stock managers, business managers, and the owner.

## Features

- Role-based access control (Salesperson, Stock Manager, Business Manager, Owner)
- Delivery and route management
- Inventory and stock auditing
- Order lifecycle tracking
- Financial transactions and reporting
- KPI targets and notifications
- Automatic end-of-day reconciliation — matches deliveries made, stock that left the warehouse, and payments collected so the books close without manual calculation

---

## Getting Started

### For New Contributors

Complete setup from scratch — follow every step.

**Prerequisites**
- Python 3.12+
- Git
- A [Neon](https://neon.tech) account (free tier works) for the database

**1. Clone the repo**
```bash
git clone <repo-url>
cd sbooks
```

**2. Create a virtual environment**

A virtual environment keeps this project's dependencies isolated from the rest of your machine.

```bash
python -m venv venv
```

**3. Activate the virtual environment**

```bash
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

Your terminal prompt will show `(venv)` when it's active. Always activate before working on this project.

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Set up environment variables**

Create a `.env` file in the `sbooks/` folder:

```
DATABASE_URL=your-neon-connection-string-here
JWT_SECRET=your-secret-key-here
```

To generate a secure JWT secret:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

**6. Run the server**

```bash
uvicorn app.main:app --reload
```

API available at `http://localhost:8000`.

---

### For the Project Owner (Returning Sessions)

Assumes the repo is already cloned and `.env` is already populated.

```bash
cd sbooks
source venv/bin/activate        # Mac/Linux
uvicorn app.main:app --reload
```

> If you ever get `ModuleNotFoundError`, your venv may not be active or dependencies may have changed — run `pip install -r requirements.txt` again.

---

### Production Deployment

In production, **do not use a `.env` file**. Instead, set environment variables directly on your server or hosting platform. The app reads them the same way — the difference is just where they live.

**Option A — Set on the server directly (VPS/SSH)**

```bash
export DATABASE_URL="your-neon-connection-string-here"
export JWT_SECRET="your-secret-key-here"
```

To make them persist across reboots, add the above lines to your `~/.bashrc` or `~/.bash_profile`.

**Option B — Modal (recommended for this project)**

In your Modal deployment script, pass secrets via Modal's secret store:

```python
import modal
app = modal.App("sbooks")
secret = modal.Secret.from_name("sbooks-secrets")
```

Create the secret once via the Modal dashboard or CLI:
```bash
modal secret create sbooks-secrets DATABASE_URL="..." JWT_SECRET="..."
```

**Option C — Any platform with env var support (Railway, Render, Fly.io, etc.)**

Set `DATABASE_URL` and `JWT_SECRET` in the platform's environment variables dashboard — no `.env` file needed.

---

**Generating a secure JWT secret (any environment)**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
