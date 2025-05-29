# tchat

This project is part of the [udemyChatGPTcourse](https://github.com/alianwaar73/udemyChatGPTcourse) repository and demonstrates building a terminal-based chatbot using LangChain, OpenAI, and conversation memory.

---

## Environment Setup

This project uses **Python 3.11** and manages dependencies with [Pipenv](https://pipenv.pypa.io/en/latest/).

### 1. Install Pipenv (if not already installed)
```bash
pip install pipenv
```

### 2. Install dependencies and create environment
Run this in the project root or `pycode/` directory (where the `Pipfile` is present):
```bash
pipenv install
```

### 3. Enter the virtual environment
```bash
pipenv shell
```

### 4. Add your OpenAI API key
Create a `.env` file in this directory with:
```
OPENAI_API_KEY=your-api-key-here
```

### 5. Exit the virtual environment
Simply type:
```bash
exit
```

---

## Features

- **Terminal Chatbot:** Engage in a persistent conversation with an AI assistant in your terminal.
- **Conversation Memory:** Uses `ConversationSummaryMemory` to summarize and remember previous messages for a natural, context-aware chat experience.
- **Session Persistence:** Optionally (with minor code changes), you can use `FileChatMessageHistory` to persist chat history to a file, allowing conversations to resume across sessions.
- **Verbose Debugging:** The `verbose=True` flag on the language model and chain shows conversation summaries as system messages for easier debugging.
- **Prompt Engineering:** Utilizes LangChain's chat prompt templates, including human message and memory placeholders, for flexible conversation design.

---

## Usage

To start a chat session, run:

```bash
python pycode/tchat/main.py
```
Type your messages at the prompt (`>> `). The assistant will respond, maintaining context from earlier in the session and, with appropriate configuration, across sessions.

---

## File Structure

- `main.py` – Core chatbot script using LangChain, OpenAI, and conversation memory.

---

## Implementation Notes

This project contains detailed code comments explaining:
- The use of LangChain's chat models and memory components (`ConversationSummaryMemory` by default for cost-effectiveness; `ConversationBufferMemory` and `FileChatMessageHistory` as alternatives for different persistence options).
- How prompts are constructed for conversational AI, using message placeholders and user input templates for flexible, memory-integrated dialogue.
- The role of verbose/debug flags to display system messages and summaries during development.
- How to wire memory into chains for persistent, natural conversations.

You can review the code comments in `main.py` for further learning and clarification.

---

## Requirements

- Python 3.11
- Pipenv
- OpenAI account and API key

---

> _This README was generated and updated by GitHub Copilot AI._