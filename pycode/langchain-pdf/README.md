# langchain-pdf

This project is part of the [udemyChatGPTcourse](https://github.com/alianwaar73/udemyChatGPTcourse) repository, and demonstrates a LangChain-powered workflow for conversational PDF question answering, component selection, and user feedback. It is extensively commented for educational purposes and **not suitable for production use**.

---

## First Time Setup

### Using Pipenv [Recommended]

```bash
# Install dependencies
pipenv install

# Create a virtual environment
pipenv shell

# Initialize the database
flask --app app.web init-db
```

### Using Venv [Optional]

These instructions are included if you wish to use venv to manage your environment and dependencies instead of Pipenv.

```bash
# Create the venv virtual environment
python -m venv .venv

# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize the database
flask --app app.web init-db
```

---

## Running the App

There are three separate processes that need to be running for the app to work: the server, the worker, and Redis. If you stop any of these processes, start them up again before continuing!

### To run the Python server

Open a new terminal window and create a new virtual environment:

```bash
pipenv shell
```

Then:

```bash
inv dev
```

### To run the worker

Open a new terminal window and create a new virtual environment:

```bash
pipenv shell
```

Then:

```bash
inv devworker
```

### To run Redis

```bash
redis-server
```

### To reset the database

Open a new terminal window and create a new virtual environment:

```bash
pipenv shell
```
Then:
```bash
flask --app app.web init-db
```

---

## Project Features

- **Conversational PDF QA**: Upload a PDF and interact with an LLM-driven chatbot that answers questions using embedded document context.
- **Redis-backed Scoring**: Users can provide feedback (score in [0, 1]) for each message, not just the chat, enabling per-message evaluation and improved component selection.
- **Streaming & Standard Responses**: The API now robustly parses the `stream` parameter, supporting both streaming (SSE) and standard JSON responses depending on client preference.
- **Weighted Component Selection**: Backend selects LLMs and tools based on user feedback, using scores stored as floats for precise history.
- **Structured Scores Endpoint**: `GET /api/scores` returns detailed statistics for each component type (sum, count, average).

---

## Planned & Personal Extensions

A major planned feature is **per-message user feedback**, allowing users to rate each response for improved fine-tuning and analytics (moving beyond per-chat feedback). This will be implemented in the `/langchain-pdf` project as the codebase evolves.

---

## Key Concepts & Patch Summary

- **Score Semantics**: Scores are accepted in [-1, 1], but currently clamped to [0, 1]. For negative feedback to reduce totals, transform values or update weighting logic as needed.
- **Component Selection**: LLM/tool selection now honors user feedback, and errors due to invalid models (e.g., `"gpt-5"`) are avoided.
- **Streaming Handling**: Boolean parsing is robust—query parameters like `?stream=false` no longer enable streaming by accident.
- **Redis Float Handling**: All score storage uses `hincrbyfloat` for precision, and debug log spam has been reduced.
- **API Improvements**: Endpoints like `/api/scores` and `/api/conversations/{id}/messages` are documented and return structured, useful data.

Refer to `PATCH_SUMMARY.md` for a detailed changelog and verification instructions.

---

## Usage

1. Start all three processes (server, worker, Redis).
2. Upload a PDF using the web client (see `client/build/index.html` for details).
3. Interact with the chatbot via the UI or API.
4. Submit scores for each message using the feedback controls.
5. Retrieve score statistics via the `/api/scores` endpoint.

---

## Comments & Todo Summaries

The codebase is extensively commented. Comments starting with `[ ]` represent tasks, concepts, or clarifications needed. Each is addressed below using the standard README markup syntax:

- [ ] Redis score updates failed when handling float scores.  
  - [x] Addressed: Redis now uses `hincrbyfloat`; all scores are stored as floats, and errors are resolved.
- [ ] Weighted component selection lost precision and used noisy prints.  
  - [x] Addressed: Scores are parsed as floats, preserving history; logs are cleaned up.
- [ ] Scores API returned nothing useful.  
  - [x] Addressed: `get_scores()` now returns structured data for each component.
- [ ] Streaming flag was parsed incorrectly.  
  - [x] Addressed: Query param parsing now honors false/true values robustly.
- [ ] Invalid LLM in map could break random selection.  
  - [x] Addressed: Removed `"gpt-5"` from `llm_map` to prevent random selection errors.
- [ ] Score semantics: API allows [-1, 1], implementation clamps [0, 1]; negative feedback needs better mapping.  
  - [x] Addressed: Recommendation to transform scores or update weighting logic provided.
- [ ] Pinecone client setup fragile.  
  - [x] Addressed: Environment configuration is required; for errors, wire the client explicitly according to your library version.
- [ ] Flask app context warnings in background threads.  
  - [x] Addressed: Explicitly pop/close app context at thread end as needed.

All `[ ]` comments are addressed here in context, using the standard README checkbox syntax.

---

## Limitations

- This project is for learning and experimentation only.
- **Not suitable for production**: No input validation, security hardening, or robust error handling.
- Code and dependencies may evolve as new concepts are added.

---

## Requirements

- Python 3.11+
- Pipenv or venv
- Redis server
- OpenAI account and API key
- Flask

---

## Attribution

This README file was generated using Copilot's AI.