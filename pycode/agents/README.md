# Agents Project (LangChain + SQLite)
_A practical, course-driven deep dive into agents, tools, and prompt engineering for LLM-powered database querying._

---

## Overview

This project exemplifies the use of **LangChain Agents** to autonomously answer natural language questions by leveraging tools—primarily, a custom SQL tool—against a SQLite database. The codebase is structured for educational clarity and reproducibility, with intentional backup snapshots and detailed, actionable comments.

---

## Agents in this Project: Contextual Primer

### What is an Agent?

In the LangChain context, an **Agent** is an orchestrator powered by an LLM (such as OpenAI's GPT models) that decides **if/when/how** to use external tools (like SQL queries) to fulfill a user's request. Agents analyze user input, reason through the necessary steps, and interact with tools in multi-turn workflows, using intermediate results to iteratively build towards an answer.

**In this project:**  
- The agent receives a user query (e.g., "How many users are there?").
- It chooses whether to answer directly or invoke a tool (e.g., a SQL database).
- The agent outputs the final answer after processing.

#### Why are agents needed?

LLMs alone can't interact with external systems (like databases). Agents bridge this gap, enabling LLMs to **act** in the world by leveraging tools—enabling workflows beyond pure text generation.

---

### General Agent Workflow (with Project-Specific Context)

```
┌────────────────────┐
│  User Query/Input  │
└─────────┬──────────┘
          │
          ▼
┌───────────────────────────────┐
│    LLM Agent (LangChain)      │
│   (OpenAIFunctionsAgent)      │
└─────────┬───────────┬─────────┘
          │           │
          ▼           ▼
   Use Tools?    Answer Directly?
(SQL, etc)      (if possible)
     │
     ▼
┌───────────────────────────────┐
│   Tool (SQL Query, Schema)    │
│ (run_sqlite_query, etc)       │
└─────────┬─────────────────────┘
          │
          ▼
    ┌─────────────┐
    │ SQLite DB   │
    └─────┬───────┘
          │
          ▼
┌───────────────────────────────┐
│   Query Result / Final Answer │
└───────────────────────────────┘
```

_**Note:** Each block represents a step; the agent may loop through the process, refining its actions based on intermediate results ("agent scratchpad"), until the answer is built._

---

## File Structure

- **main.py** – Current main entrypoint. Sets up the agent and its tools, engineers the prompt (with database schema awareness), and demonstrates agent execution.
- **tools/sql.py** – Implements the SQL tools, including query execution, schema listing, and table description. All tool logic and database connection are here.
- **backups/main_backup.py** – A preserved, reproducible snapshot of a prior state (see [Reproducibility & Backups](#reproducibility--backups)).
- **Pipfile / Pipfile.lock** – For dependency management (Python 3.11, Pipenv).
- **db.sqlite** – The SQLite database (ensure this is present for all operations).

More files may exist, e.g., for experiment tracking or addenda (see code).

---

## Environment Setup

1. **Install Pipenv**  
   ```bash
   pip install pipenv
   ```
2. **Install dependencies**  
   ```bash
   pipenv install
   ```
3. **Activate environment**  
   ```bash
   pipenv shell
   ```
4. **Set OpenAI API Key**  
   Create a `.env` file with:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
5. **Prepare the Database**  
   Ensure `db.sqlite` exists with relevant tables (e.g., `users`). You may add more tables for experimentation.

---

## Usage

```bash
python main.py
```

- The agent will process your query (as set in main.py), decide on tool usage, interact with the SQLite database, and return the result.
- You can modify the query to observe different agent behaviors.

---

## Key Concepts & Implementation Details

### What is a Tool?
A **Tool** is a wrapper exposing a capability (function, API, DB query) to the agent.  
- Each tool has a `name`, `description`, and `func`.
- In this project, the main tools are:
  - `run_sqlite_query` — executes arbitrary SQL queries.
  - `list_tables` and `describe_tables` — provide schema awareness to the agent.

**Why Tools?**  
They let agents interact with the world, turning LLMs into actionable assistants (e.g., answering data questions).

### Agent Scratchpad: What and Why?

- The **agent_scratchpad** is a memory space used by the agent to track intermediate steps, tool invocations, and reasoning chains.
- **In practice:** The scratchpad records each step the agent takes—what tool it tried, what result it received—enabling multi-step reasoning and course correction.
- **In this project:**  
  - The scratchpad is managed via LangChain’s `MessagesPlaceholder`.
  - It enables the agent to “think aloud,” try different queries, and converge on the correct database interaction—even when initial attempts fail.
  - This is especially visible when the agent tries to query a table that may not exist (see prompt engineering notes below).

### Prompt Engineering & Schema Awareness

- Early versions of the agent assumed the presence of certain tables (e.g., `users`), leading to errors.
- The code was enhanced (see `main.py`, `tools/sql.py`) to provide **database schema information** to the agent at prompt-time, reducing failed queries and guesswork.
- Capturing and relaying errors from failed queries back to the agent allows adaptive, convergent reasoning.

---

## [ADDENDUM] On Course Progress & Concept Introduction

- **[ADDENDUM]** comments in the code mark points where new concepts are introduced (e.g., improved toolset, schema-awareness, error handling).
- The project evolves as the course progresses; backup files (see below) are used to snapshot major conceptual milestones for comparison and reproducibility.

---

## Reproducibility & Backups

- **Why backup files?**  
  - Files like `main_backup.py` are intentionally created to **preserve a snapshot** of the code at a specific point (e.g., before a major logic change).
  - This allows you to **reproduce and compare** agent behavior at different stages of the course or code evolution.

- **How to use?**  
  - To reproduce an older state, simply run the backup file (e.g., `python backups/main_backup.py`).
  - Compare output and agent reasoning with the current `main.py` to understand the impact of code changes (such as improved prompt engineering or schema-awareness).

---

## Addressing Todo Comments

Below, all `[ ]` (todo) comments from the codebase are listed and **addressed**:

- [ ] The README should contain a description of Tool. Why it came into being and what purpose does it serve.  
  - [x] Addressed in “What is a Tool?” section above.

- [ ] Some background on sqlite package specifically the variables used in the following such as what is "c" and general description of the following function in README  
  - [x] `sqlite3` is Python’s built-in library for working with SQLite.  
    - `conn` is the database connection (via `sqlite3.connect()`).
    - `c` is a cursor (`conn.cursor()`), used to execute SQL statements and fetch results.
    - The `run_sqlite_query(query)` function executes a SQL query and returns results (or error message).

- [ ] Include some description of agents in the README  
  - [x] Extensive explanations are provided in the “Agents in this Project” section.

- [ ] The README should contain some description around this link [tools/sql.py].  
  - [x] Described in “File Structure” and "What is a Tool?" sections. `tools/sql.py` defines all database interaction tools and their wrappers.

- [ ] <Investigate> The following query works given the HUGE assumption made by the ChatGPT where it assumes a table named 'users' which happens to be there in our db. But fails when something like 'shipping address' is queried! Raising the need to modify our sql.py (done) so that ChatGPT is context-aware about our db without making assumptions about its structure on its own!  
  - [x] Investigated above; the agent’s limitations stem from a lack of schema awareness. This was addressed by adding schema information to the agent prompt and providing schema-related tools. This allows the agent to adaptively discover and use the actual structure of your database, rather than guessing.

- [ ] Also, observing the output of the following query is VERY INSIGHTFUL! Shows the process in which the agent eventually figures out the way to correctly interact with our db!!!  
  - [x] This is a product of the agent's multi-step reasoning, captured via the agent_scratchpad. The agent tries, receives errors, and adapts—demonstrating prompt engineering and tool-chaining in action.

- [ ] Also, include in the README if this figuring out convergence is handled by the agent_scratchpad?  
  - [x] Addressed above in "Agent Scratchpad" section. The scratchpad logs each step/reasoning/error, allowing the agent to “learn” and correct itself mid-execution.

---

## Example: Tool and Agent Flow

**User:** "How many users are in the database?"

1. The agent receives the question.
2. It decides to use the SQL tool.
3. The SQL tool runs: `SELECT COUNT(*) FROM users;`
4. The result is returned and the agent outputs: "There are 123 users in the database."

---

## Limitations

- This code is for educational demonstration only.
- No input validation or SQL injection prevention—**do not use in production**.
- The agent is limited by the capabilities of the selected LangChain and OpenAI API versions.

---

## Requirements

- Python 3.11
- Pipenv
- OpenAI account/API key
- SQLite database (`db.sqlite`)

---

> _This README was generated and updated using Copilot's AI. All todo comments in code files have been summarized, addressed, and clarified per project instructions. For further detail or unresolved todos, see the codebase or [full code search results](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=%5B+%5D+OR+%5BIMPORTANT%5D+OR+%3CInvestigate%3E+OR+%5BADDENDUM%5D+path%3Apycode%2Fagents%2F)._