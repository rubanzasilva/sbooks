# Session Tracking & Cleanup — Industry Standard Practices
**Created:** 2026-03-22

---

## 1. Progress Tracking Options

| Approach | When to Use |
|----------|------------|
| **`PROGRESS.md` in repo** | Solo dev / small team, keeps tracking close to code |
| **GitHub Issues + Projects board** | Kanban/sprint boards, assignees, labels — free and integrated with repo |
| **Linear / Jira / Notion** | Team settings, more structure, sprint velocity tracking |
| **CHANGELOG.md** | For tracking *releases*, not dev progress — different purpose |

**Current choice for Sbooks:** `PROGRESS.md` in repo (see `PROGRESS.md`)

---

## 2. End-of-Session Cleanup (What Good Developers Do Before Closing the Laptop)

### Commit Work-in-Progress (WIP)
```bash
git add -A && git commit -m "WIP: description of where I left off"
```
Never leave uncommitted work overnight.

### Push to Remote
Protects against local machine failure. Always push before ending session.

### Update Your Tracker
2 minutes of session notes saves 20 minutes of "where was I?" next time. Use the Session Log in `PROGRESS.md`.

### Clean Up Branches
Delete merged branches, rebase if needed.
```bash
git branch --merged | grep -v main | xargs git branch -d
```

### Close Running Servers/Processes
Avoid port conflicts next session.

### Leave a Breadcrumb
Leave a `# TODO: NEXT SESSION - ...` comment at the exact line you stopped at.

---

## 3. More Structured Approaches (For When the Project Grows)

### GitHub Issues as Sprint Items
- Create one issue per sprint task
- Close them as you go
- Use milestones for sprints
- Gives you a visual Kanban board for free

### Git Stash with Messages
```bash
git stash push -m "halfway through auth middleware"
```
Use when you don't want WIP commits polluting history.

### ADR (Architecture Decision Records)
```
/docs/decisions/001-chose-neon-over-supabase.md
```
Tracks *why* you made choices. Invaluable when revisiting decisions months later.

### Conventional Commits
Structured commit messages that enable automated changelogs:
```
feat(auth): add JWT token refresh endpoint
fix(inventory): correct stock count on partial delivery
chore(deps): update fastapi to 0.109.0
```

### Pre-commit Hooks
Automate quality checks before every commit:
- Linting (ruff/flake8)
- Formatting (black/ruff format)
- Type checking (mypy)
- Secret scanning (detect-secrets)

---

## Recommended Setup for Sbooks (Current Stage)

You're solo, early phase. Keep it simple:

1. **`PROGRESS.md`** — update the session log each time (already in place)
2. **GitHub Issues** — for sprint tasks, gives you a visual board
3. **WIP commits + push** — at end of every session
4. **Breadcrumb comments** — `# TODO: NEXT SESSION` at stopping points
