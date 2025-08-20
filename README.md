# udemyChatGPTcourse

This repository is a follow-up to Udemy's ChatGPT course, extensively commented and structured for learners. It is **not** intended for production use. The codebase has evolved to contain multiple mini-projects and experiments, each exploring LLMs, LangChain, prompt engineering, agents, and tool integration. Personal improvements and additional features are being incrementally added, including a per-message feedback system in the `/langchain-pdf` project.

---

## Quick Start: Environment Setup

### Linux & Windows

#### 1. Clone the Repository

```bash
git clone https://github.com/alianwaar73/udemyChatGPTcourse.git
cd udemyChatGPTcourse
```
#### 2. Install Python (Recommended: 3.11+)

- **Linux:** Use `sudo apt install python3.11`
- **Windows:** Download from [python.org](https://www.python.org/)

#### 3. Install Pipenv

```bash
pip install pipenv
```

#### 4. Install Project Dependencies

At the root (or inside a project subfolder with its own `Pipfile`):

```bash
pipenv install
```

#### 5. Activate the Virtual Environment

```bash
pipenv shell
```

#### 6. Add Your OpenAI API Key

Create a `.env` file in the relevant folder:

```
OPENAI_API_KEY=your-api-key-here
```

#### 7. Exit the Virtual Environment

```bash
exit
```
or
```bash
pipenv exit
```

---

## Repository Structure

- `/pycode`: Core Python scripts for code and test generation, chatbots, and agent-based workflows.
  - `/agents`: LangChain agents for SQLite querying, prompt engineering, and custom handlers.
  - `/tchat`: Conversational chatbots with memory.
- `/langchain-pdf`: (Planned) Per-message user feedback system for PDF-based LLM workflows.
- `/tools`: Utilities and helper scripts. Extra personal project. Not relevant to the course.
- `/CompletionCertificate`: Course completion artifacts.
- `/Udemy_diagrams`: Visual diagrams for course concepts.
- `scores.ipynb`: Jupyter notebook for experimentation.
- `AGENTS.md`: Created by OpenAI's codex-cli. Not relevant to the course contents.

---

## Main Features

- **Automated Code/Test Generation:** Use LangChain and OpenAI to create code snippets and matching tests in multiple languages.
- **LLM Agents:** Autonomous agents that use external tools (like SQL) to answer user queries.
- **Prompt Engineering:** Customizable prompts for improved results.
- **Conversational Memory:** Persistent context in chatbots.
- **Custom Handlers:** Visualize agent reasoning and tool usage in the terminal.
- **Experiment Tracking:** Backup scripts and extensive comments for learning progression.

---

## Example Usage

Generate code and test:
```bash
python pycode/main.py --language javascript --task 'print hello'
```

Start a chatbot:
```bash
python pycode/tchat/main.py
```

Run an agent for querying a SQLite database:
```bash
cd pycode/agents
python main.py
```

---

## Key Concepts

### Agents

Agents are orchestrators powered by LLMs that decide **if/when/how** to use external tools (e.g., databases) to answer user questions. They bridge the gap between pure text generation and actionable workflows.

### Tools

Tools are wrappers that expose specific capabilities (SQL queries, report writing, etc.) for the agent to use. Each tool has a `name`, `description`, and a callable function. This enables agents to interact with external systems and provide meaningful answers.

### Handlers

Custom handlers (e.g., in `chat_model_start_handler.py`) intercept agent execution events, visually box messages in the terminal, and provide debugging insights into agent reasoning and tool usage.

### Agent Scratchpad

A memory space for agents to track intermediate steps, tool invocations, and reasoning chains, enabling multi-step problem solving and adaptive behaviors.

---

## Todo Comments Addressed

All `[ ]` (todo) comments from the codebase are **addressed** below following standard README task-list syntax:

- [ ] The README should contain a description of Tool. Why it came into being and what purpose does it serve.
  - [x] Tools allow agents to interact with external systems, enabling actionable workflows beyond text generation. Each tool exposes a specific capability (see "Tools" section).
- [ ] Some background on sqlite package specifically the variables used such as "c" and general description of the function.
  - [x] `sqlite3` is Python’s built-in library for SQLite. `conn` is the connection, `c` is the cursor for executing SQL. Functions like `run_sqlite_query` execute queries and fetch results.
- [ ] Include some description of agents in the README.
  - [x] See "Agents" section above for detailed explanation.
- [ ] The README should contain some description around tools/sql.py.
  - [x] `tools/sql.py` defines SQL tools for the agent, including query execution and table/schema discovery.
- [ ] Ask the AI in detail about the handler branch for `message.type == "ai" and "function_call" in message.additional_kwargs`.
  - [x] This handler intercepts OpenAI function calls, extracts function names/arguments, and displays them in color-coded boxes for debugging and transparency.
- [ ] It informs LangChain to use an argument called query (instead of the default __arg1) in its source code.
  - [x] Custom Pydantic schema classes (e.g., `RunQueryArgsSchema`) clarify argument passing, making tool invocation more natural and explicit for the agent.

---

## Limitations

- This repository is for learning and experimentation only.
- **Not production-ready**: No input validation, security hardening, or robust error handling.
- Code and dependencies evolve as new concepts are added or improved.

> **Note:** For all personal extensions, including the planned per-message feedback feature in `/langchain-pdf`, refer to project subfolders for detailed instructions.

---

## Requirements

- Python 3.11+
- Pipenv
- OpenAI account/API key
- (For agents) SQLite database (`db.sqlite`)

---

## License & Attribution

This repository is for educational purposes only.

**This README file was generated using Copilot's AI.**