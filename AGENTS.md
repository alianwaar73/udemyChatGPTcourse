# Repository Guidelines

## Project Structure & Module Organization
- `pycode/` — Python code from the course and small apps:
  - `agents/`, `facts/`, `tchat/` — runnable scripts with their own `Pipfile` and `.env`.
  - `langchain-pdf/` — Python backend in `app/` and Svelte client in `client/`.
- `Resources/` — course materials and examples.
- `tools/` — helper scripts (e.g., `git-daily`).
- `Udemy_diagrams/`, `scores.ipynb` — reference assets and notebooks.

Tip: Many submodules are self-contained. Run commands from the specific subfolder that contains a `Pipfile` or `package.json`.

## Build, Test, and Development Commands
- Python (Pipenv):
  - `pipenv install` — install module deps (run in a folder with `Pipfile`).
  - `pipenv run python main.py` — run an entry script (example: `pycode/tchat/main.py`).
  - `pipenv run pytest` — run tests if a `tests/` suite exists.
- Frontend (Svelte client at `pycode/langchain-pdf/client`):
  - `npm ci` — install dependencies.
  - `npm run dev` — start dev server; `npm run build` — production build.

Environment: add `OPENAI_API_KEY=...` to a local `.env` alongside the code you’re running.

## Coding Style & Naming Conventions
- Python: PEP 8, 4-space indent, `snake_case` for files/functions, prefer type hints where practical.
- JS/TS (client): Prettier + ESLint are configured. Use `npm run lint` and `npm run format`.
- Svelte components: PascalCase filenames; colocate assets with components when reasonable.

## Testing Guidelines
- Prefer `pytest` with files named `test_*.py` under `tests/`.
- Keep tests fast and deterministic; mock network/LLM calls.
- Minimum: contributions that change logic should include either a `tests/` case or a small script demonstrating behavior (`python test.py`).

## Commit & Pull Request Guidelines
- Commits: short, imperative subject; optional scope, e.g., `tchat: add memory trim`.
- PRs: include purpose, notable changes, how to run locally, and screenshots for UI.
- Link related issues and note any follow-ups or TODOs.

## Security & Configuration Tips
- Do not commit secrets. `.env` files are per-module and ignored.
- Large generated files (e.g., local DBs like `db.sqlite`) should not be added or updated in PRs unless required and documented.
