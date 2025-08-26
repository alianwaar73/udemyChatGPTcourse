# Agents Project (LangChain + SQLite)
_A practical, course-driven deep dive into agents, tools, prompt engineering, and custom handlers for LLM-powered database querying._

> _✨ AI tip: This project is annotated and structured to maximize discoverability, learning, and reproducibility. Jump directly to these codebase flags: [\[ADDENDUM\]](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=%5BADDENDUM%5D+path%3Apycode%2Fagents%2F), [\[ \]](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=%5B+%5D+path%3Apycode%2Fagents%2F), or [\<Investigate\>](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=%3CInvestigate%3E+path%3Apycode%2Fagents%2F) for educational milestones and deep dives!_

---

## Overview

This project exemplifies the use of **LangChain Agents** to autonomously answer natural language questions by leveraging tools—primarily, a custom SQL tool—against a SQLite database. The codebase is structured for educational clarity and reproducibility, with intentional backup snapshots, detailed, actionable comments, and now features custom handler integration for enhanced output and debugging.

> _💡 As you explore, keep an eye out for [ADDENDUM](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=%5BADDENDUM%5D+path%3Apycode%2Fagents%2F), [IMPORTANT](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=%5BIMPORTANT%5D+path%3Apycode%2Fagents%2F), and [ ](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=%5B+%5D+path%3Apycode%2Fagents%2F) comments in the code. These serve as a guided tour and a living learning log!_

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

> _🔎 Curious about the underlying code or evolution of this logic? Jump to [Agent](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=Agent+path%3Apycode%2Fagents%2F) or [OpenAIFunctionsAgent](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=OpenAIFunctionsAgent+path%3Apycode%2Fagents%2F) references for direct context!_

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
│   Tool (SQL Query, Schema,    │
│   Report, etc)                │
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

_**Note:** Each block represents a step; the agent may loop through the process, refining its actions based on intermediate results ("agent scratchpad"), until the answer is built. With handlers, the process is now even more transparent and visually informative (see below)._

---

## File Structure

- **[main.py](https://github.com/alianwaar73/udemyChatGPTcourse/blob/main/pycode/agents/main.py)** – Main entrypoint, now integrates custom handlers, tools, and prompt engineering. Demonstrates agent execution and memory.
- **[tools/sql.py](https://github.com/alianwaar73/udemyChatGPTcourse/blob/main/pycode/agents/tools/sql.py)** – SQL tools: query execution, schema discovery, and argument schemas for more robust agent-tool interaction.
- **[tools/report.py](https://github.com/alianwaar73/udemyChatGPTcourse/blob/main/pycode/agents/tools/report.py)** – HTML report writing tool (StructuredTool): lets the agent generate and write HTML files to disk.
- **[handlers/chat_model_start_handler.py](https://github.com/alianwaar73/udemyChatGPTcourse/blob/main/pycode/agents/handlers/chat_model_start_handler.py)** – **New!** Custom callback handler to visually render agent interactions, making debugging and learning more intuitive.
- **[backups/main_backup.py](https://github.com/alianwaar73/udemyChatGPTcourse/blob/main/pycode/agents/backups/main_backup.py)** – Preserved snapshot for reproducibility.
- **[Pipfile](https://github.com/alianwaar73/udemyChatGPTcourse/blob/main/pycode/agents/Pipfile) / [Pipfile.lock](https://github.com/alianwaar73/udemyChatGPTcourse/blob/main/pycode/agents/Pipfile.lock)** – For dependency management.
- **db.sqlite** – SQLite database (ensure this is present).

> _🗂️ Files in [`backups/`](https://github.com/alianwaar73/udemyChatGPTcourse/tree/main/pycode/agents/backups) are like checkpoints—run them to “time travel” and see how the agent’s behavior and learning evolved! For new users, these are great for comparison and experimentation._

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
6. **Exit the Virtual Environment**  
   When you are done working in the pipenv shell, you can exit the virtual environment by running:
   ```bash
   exit
   ```
   or
   ```bash
   pipenv exit
   ```

> _✨ For context? Jump to [todo flags](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=%5B+%5D+path%3Apycode%2Fagents%2F), [addenda](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=%5BADDENDUM%5D+path%3Apycode%2Fagents%2F), or [investigations](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=%3CInvestigate%3E+path%3Apycode%2Fagents%2F) to see why and how things changed at each step of the course!_

---

## Usage

Run the interactive agent REPL:

```bash
pipenv run python main.py
```

- Type your prompt at `You>` and press Enter. The agent will decide on tool usage (SQL/report), interact with the SQLite database, and print the final answer. Type `quit` (or `exit`, `:q`, `q`) to leave.
- The **Report tool** can be used by simply asking for a report, e.g.:

---

```python
 "List the top 50 bought products with details and write an HTML report to disk."
```

- With the custom handler, agent messages (system, human, AI, function calls) are visually boxed and color-coded for easier debugging and understanding.
- Use multiple turns in the same session; conversation memory keeps prior exchanges in context.

> _🧪 AI suggestion: To reproduce or compare previous states, run a file from [backups/](https://github.com/alianwaar73/udemyChatGPTcourse/tree/main/pycode/agents/backups). Tweak queries in any version to see how prompt engineering, tool use, and handlers have evolved!_

---

## Key Concepts & Implementation Details

### What is a Tool?
A **Tool** is a wrapper exposing a capability (function, API, DB query) to the agent.  
- Each tool has a `name`, `description`, and `func`.
- In this project, the main tools are:
  - [`run_sqlite_query`](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=run_sqlite_query+path%3Apycode%2Fagents%2F) — executes arbitrary SQL queries.
  - [`list_tables`](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=list_tables+path%3Apycode%2Fagents%2F) and [`describe_tables`](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=describe_tables+path%3Apycode%2Fagents%2F) — provide schema awareness.
  - [`write_report`](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=write_report+path%3Apycode%2Fagents%2F) — lets the agent write HTML reports to disk.

**Why Tools?**  
They let agents interact with the world, turning LLMs into actionable assistants (e.g., answering data questions, generating reports).

> _🤖 Want to dive deeper? [See all uses of `run_sqlite_query`](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=run_sqlite_query+path%3Apycode%2Fagents%2F) in the codebase to jump to its definition or usages!_

### Agent Scratchpad: What and Why?

- The **agent_scratchpad** is a memory space used by the agent to track intermediate steps, tool invocations, and reasoning chains.
- **In practice:** The scratchpad records each step the agent takes—what tool it tried, what result it received—enabling multi-step reasoning and course correction.
- **In this project:**  
  - The scratchpad is managed via LangChain’s `MessagesPlaceholder`.
  - It enables the agent to “think aloud,” try different queries, and converge on the correct database interaction—even when initial attempts fail.
  - This is especially visible when the agent tries to query a table that may not exist (see prompt engineering notes below).

> _🪄 Note: Curious how the agent “learns” from its errors and retries? Search for [scratchpad](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=scratchpad+path%3Apycode%2Fagents%2F) or step through the verbose output in the terminal to observe this in action!_

### Prompt Engineering & Schema Awareness

- Early versions of the agent assumed the presence of certain tables (e.g., `users`), leading to errors.
- The code was enhanced (see [main.py](https://github.com/alianwaar73/udemyChatGPTcourse/blob/main/pycode/agents/main.py), [tools/sql.py](https://github.com/alianwaar73/udemyChatGPTcourse/blob/main/pycode/agents/tools/sql.py)) to provide **database schema information** to the agent at prompt-time, reducing failed queries and guesswork.
- Capturing and relaying errors from failed queries back to the agent allows adaptive, convergent reasoning.

> _🔍 The history of these improvements can be tracked in the [ADDENDUM](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=%5BADDENDUM%5D+path%3Apycode%2Fagents%2F) comments and backup files. For a before/after, compare [`main_backup.py`](https://github.com/alianwaar73/udemyChatGPTcourse/blob/main/pycode/agents/backups/main_backup.py) and [`main.py`](https://github.com/alianwaar73/udemyChatGPTcourse/blob/main/pycode/agents/main.py)!_

---

## Handlers: Custom Output & Debugging

### What are Handlers?

Handlers in LangChain are callback hooks that let you intercept and respond to various stages of the agent's execution (such as when a model starts, a tool is called, etc.). This project introduces a custom handler:

- **[handlers/chat_model_start_handler.py](https://github.com/alianwaar73/udemyChatGPTcourse/blob/main/pycode/agents/handlers/chat_model_start_handler.py)**
  - Subclasses `BaseCallbackHandler`.
  - Intercepts the `on_chat_model_start` event.
  - Uses `pyboxen` to render system, human, AI, function, and tool call messages in colored boxes in the terminal, making agent reasoning and tool usage visually transparent.

#### [ ] Ask the AI in detail about the following one in README

**Handler logic for message.type == "ai" and "function_call" in message.additional_kwargs:**

This branch handles when the AI model (e.g., GPT) decides to invoke a tool/function via an OpenAI-style function call.  
- It extracts the function name and arguments from the message, and prints a visually distinct, color-coded box with this info.
- This allows you to see, step-by-step, when and how the agent delegates to tools, what arguments it provides, and what is being executed.

**In summary:**  
- This approach provides pedagogical and debugging value by giving immediate, readable feedback on the agent's internal “thought process” and tool usage.
- For other message types (system, human, AI, function), the handler color-codes and displays the content for clarity.

> _📦 Handlers are your window into the agent’s inner workings—watch the terminal to see every tool call, system message, and response as a color-coded, boxed log._

---

## [ADDENDUM] On Course Progress & Concept Introduction

- **[ADDENDUM]** comments in the code mark points where new concepts are introduced (e.g., improved toolset, schema-awareness, error handling).
- The project evolves as the course progresses; backup files (see below) are used to snapshot major conceptual milestones for comparison and reproducibility.

> _🚦 Use [ADDENDUM](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=%5BADDENDUM%5D+path%3Apycode%2Fagents%2F) comments as signposts for the project's journey—each one marks a new conceptual level or key learning moment!_

---

## Reproducibility & Backups

- **Why backup files?**  
  - Files like [`main_backup.py`](https://github.com/alianwaar73/udemyChatGPTcourse/blob/main/pycode/agents/backups/main_backup.py) are intentionally created to **preserve a snapshot** of the code at a specific point (e.g., before a major logic change).
  - This allows you to **reproduce and compare** agent behavior at different stages of the course or code evolution.

- **How to use?**  
  - To reproduce an older state, simply run the backup file (e.g., `python backups/main_backup.py`).
  - Compare output and agent reasoning with the current [`main.py`](https://github.com/alianwaar73/udemyChatGPTcourse/blob/main/pycode/agents/main.py) to understand the impact of code changes (such as improved prompt engineering or schema-awareness).

> _⏪ Think of the backup files as a “conceptual time machine.” Use them to explore how a single prompt, handler, or schema tweak can transform agent reasoning!_

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
  - [x] Described in “File Structure” and "What is a Tool?" sections. [`tools/sql.py`](https://github.com/alianwaar73/udemyChatGPTcourse/blob/main/pycode/agents/tools/sql.py) defines all database interaction tools and their wrappers.

- [ ] Ask the AI in detail about the handler branch for `message.type == "ai" and "function_call" in message.additional_kwargs`  
  - [x] Addressed in the Handlers section above, with a detailed explanation of this branch's purpose and value for debugging/tool transparency.

- [ ] It informs LangChain to use an argument called query (instead of the default __arg1) in its source code.  
  - [x] Addressed: The custom Pydantic schema classes (e.g., `RunQueryArgsSchema`, `WriteReportArgsSchema`) are used to clarify argument passing and make tool invocation by the agent more natural and explicit. This improves communication between the agent and the tool interface, and is explained in code comments and tool sections above.

---

## Example: Tool and Agent Flow

**User:** "How many users are in the database?"

1. The agent receives the question.
2. It decides to use the SQL tool.
3. The SQL tool runs: `SELECT COUNT(*) FROM users;`
4. The result is returned and the agent outputs: "There are 123 users in the database."
5. With handlers enabled, each step is shown in the terminal with color-coded boxed logs for system, human, AI, and tool messages.

---

## Limitations

- This code is for educational demonstration only.
- No input validation or SQL injection prevention—**do not use in production**.
- The agent is limited by the capabilities of the selected LangChain and OpenAI API versions.

> _⚠️ The focus here is on learning and experimentation. For real-world deployment, always harden your code!_

---

## Requirements

- Python 3.11
- Pipenv
- OpenAI account/API key
- SQLite database (`db.sqlite`)

---

## Planned Improvements

- Automate database prompting using argument passing at CLI.

---

> _🗺️ This README is AI-augmented with minimal human input for maximum discoverability and learning. Use it as your map. For further detail or unresolved todos, see the codebase or [full code search results](https://github.com/alianwaar73/udemyChatGPTcourse/search?q=%5B+%5D+OR+%5BIMPORTANT%5D+OR+%3CInvestigate%3E+OR+%5BADDENDUM%5D+path%3Apycode%2Fagents%2F)._
