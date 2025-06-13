# Agents Project

This project is a follow-up to an online course and **demonstrates the use of LangChain Agents to enable autonomous, tool-assisted reasoning and database interaction**. Code here is for educational purposes and **not suitable for production scenarios**. It is part of the [udemyChatGPTcourse](https://github.com/alianwaar73/udemyChatGPTcourse) repository.

---

## Overview

- **Agents** in LangChain are advanced orchestrators that use Large Language Models (LLMs) to reason and decide which _tools_ or _actions_ to execute to achieve a user’s goal.
- This project showcases how to equip an agent with a custom SQL tool, allowing it to answer natural language questions by querying a SQLite database.
- The code demonstrates **agent setup, tool integration, and end-to-end query execution**.

---

## What Are Agents? (Primer)

### Textual Explanation

**Agents** are a paradigm in LLM-powered applications where the model is _not_ just responding to prompts, but is empowered to:
- **Choose** from a set of tools (e.g., search, calculator, database).
- **Decide** what actions to take, possibly in multiple steps ("reasoning").
- **Use the results** of those actions to answer complex queries.

Agents operate like a “thinking assistant” that can:
- Parse your request (“How many users are in the database?”)
- Decide to run a SQL query to find that out
- Return the answer

**LangChain provides agent classes** like `OpenAIFunctionsAgent` which integrates OpenAI models with tool use.

---

### Visual Explanation

Below is a simple diagram of how an agent operates in the provided project context:

```
┌────────────────────┐
│  User Query/Input  │
└─────────┬──────────┘
          │
          │
          ▼
┌───────────────────────────────┐
│    LLM Agent (LangChain)      │
│ (OpenAIFunctionsAgent)        │
└─────────┬───────────┬─────────┘
          │           │
          │           │
          ▼           ▼
   Decides to:   Decides to:
   Use Tools     Answer Directly
   (SQL, etc)    (if possible)
          │
          │
          ▼
┌───────────────────────────────┐
│    Tool (SQL Query Tool)      │
│ (run_sqlite_query)            │
└─────────┬───────────┘
          │
          ▼
   ┌─────────────┐
   │ SQLite DB   │
   └─────┬───────┘
         │
         ▼
┌───────────────────────────────┐
│   Query Result / Answer       │
└───────────────────────────────┘
```

---

## Environment Setup

This project uses **Python 3.11** and dependency management via [Pipenv](https://pipenv.pypa.io/en/latest/).

1. **Install Pipenv:**
   ```bash
   pip install pipenv
   ```
2. **Install dependencies:**
   ```bash
   pipenv install
   ```
3. **Activate the environment:**
   ```bash
   pipenv shell
   ```
4. **Set up your OpenAI API key:**  
   Create a `.env` file with:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```
5. **Prepare a SQLite DB:**  
   Make sure `db.sqlite` exists and contains a table named `users` (or as appropriate for your queries).

---

## File Structure

- `main.py` – Sets up the agent, integrates the SQL tool, and demonstrates answering a question using the agent.
- `tools/sql.py` – Implements the SQL tool and defines how the agent interacts with the SQLite database using LangChain’s `Tool` abstraction.
- `Pipfile` – Dependency management.

---

## Usage

### 1. **Run the Agent**

To ask the agent a question (e.g., "How many users are in the database?"):

```bash
python main.py
```

The agent will:
- Parse your question,
- Decide that it needs to run a SQL query,
- Use the SQL tool to execute the query,
- And print the result.

---

## Key Concepts & Implementation Details

### What is a Tool?  
- A **Tool** is a wrapper that defines how an LLM agent can invoke external processes (APIs, DB queries, calculations).
- Tools have a `name`, a `description`, and a function (`func`) that does the work.
- In this project, `run_sqlite_query` is the main tool, letting the agent run arbitrary SQL on a local SQLite database.

**Why do we need Tools?**  
- LLMs on their own can't access external databases or systems.
- Tools give LLM agents the ability to interact with the world beyond text.

---

### What is an Agent?  
- An **Agent** is an orchestrator that decides _when_ and _how_ to use tools in response to user input.
- LangChain agents can "think" in steps, keep track of their process ("scratchpad"), and use tools as needed.

### How Do Agents Work? (Step by Step)
1. **Receive input** from the user
2. **Analyze** the request: Does it require tool use?
3. **If so:** Choose the best tool, generate the tool input, call it, and collect the result.
4. **Repeat** as needed (some agents can do multiple steps).
5. **Return** a final answer to the user.

---

## Addressing Todo Comments

Below, all [ ] (todo) comments from the codebase are listed and **addressed** using standard README markup syntax:

- [ ] The README should contain a description of Tool. Why it came into being and what purpose does it serve.
  - [x] Addressed above in "What is a Tool?" section. Tools let LLMs interact with external systems, enabling practical, structured applications like database querying.

- [ ] Some background on sqlite package specifically the variables used in the following such as what is "c" and general description of the following function in README
  - [x] `sqlite3` is Python’s built-in library for interacting with SQLite databases.  
    - `conn` is a connection object created via `sqlite3.connect()`, representing the database file.  
    - `c` is a cursor object (`conn.cursor()`), which is used to execute SQL statements and fetch results.
    - The function `run_sqlite_query(query)` executes the provided SQL query, fetches all results, and returns them for further processing.

- [ ] Include some description of agents in the README
  - [x] Addressed extensively in "What is an Agent?", "How Do Agents Work?", and the "Primer" sections above. A visual diagram is also provided.

- [ ] The README should contain some description around this link [tools/sql.py].
  - [x] `tools/sql.py` defines the SQL Tool, which lets the agent run SQL queries via a function. It uses LangChain’s `Tool.from_function` to expose the `run_sqlite_query` function as a tool the agent can use. This file is imported in `main.py` to provide the agent with database access.

---

## Example: Tool and Agent Flow

**User:** "How many users are in the database?"

- The agent receives the question.
- It decides to use the SQL tool.
- The SQL tool runs: `SELECT COUNT(*) FROM users;`
- The result is returned and the agent outputs: "There are 123 users in the database."

---

## Limitations

- The code is for demonstration and learning only.
- No input validation or SQL injection prevention is implemented—**do not use in production**.
- The agent is limited by the capabilities of the LangChain version and OpenAI API used.

---

## Requirements

- Python 3.11
- Pipenv
- OpenAI account/API key
- SQLite database (`db.sqlite`)

---

> _This README was generated and updated using Copilot's AI. All todo comments in code files have been summarized, addressed, and clarified per project instructions._
```