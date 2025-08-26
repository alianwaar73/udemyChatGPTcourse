# Changelog — pycode/agents

All notable changes to this module are documented here. Changes in this entry were suggested by codex-cli.

## 2025-08-26 — Interactive REPL and usability improvements (suggested by codex-cli)

### Added
- Interactive REPL in `main.py` to accept user prompts at runtime and continue until the user types `quit`/`exit`/`:q`/`q`.
- Printing of the agent's final response for each turn (in addition to the callback handler's traces).

### Changed
- Wrapped execution in `if __name__ == "__main__":` to avoid running the agent on import.
- Switched agent invocation to `agent_executor.run(...)` for better compatibility with `langchain==0.0.352`.
- Updated `README.md` Usage to document the interactive workflow and how to request HTML reports.

### Notes / Suggestions (not yet implemented)
- Tools placement: Pass tools only to `AgentExecutor` (keep `agent = OpenAIFunctionsAgent(llm=chat, prompt=prompt)`), reducing redundancy.
- SQLite lifecycle: Register `atexit.register(conn.close)` in `tools/sql.py` for graceful shutdown.
- File safety: Sanitize `write_report` filenames to avoid writing outside the intended directory when handling untrusted inputs.
- Forward compatibility: Consider migrating to `.invoke({"input": ...})` when upgrading LangChain; `.run(...)` is retained for current pin.

### Files Touched
- `main.py` — add REPL loop, main guard, and `.run(...)` usage.
- `README.md` — refresh Usage section to match interactive behavior.

