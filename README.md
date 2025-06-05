# udemyChatGPTcourse

First go through of Udemy's ChatGPT course. Lightly commented. No personal projects. [Course link](https://www.udemy.com/share/109HbI3@2jeNzCrmSShzOCAt5UMVGp3QlEZwnffD5prYbjKQYgFIqwTksjdNRUU72UkRRx[...])

---

## Environment Setup

This project uses **Python 3.11** and manages dependencies with [Pipenv](https://pipenv.pypa.io/en/latest/).

### 1. Install Pipenv (if not already installed)
```bash
pip install pipenv
```

### 2. Install dependencies and create environment
Run this in the project directory (e.g., `pycode/` or the root where a `Pipfile` is present):
```bash
pipenv install
```

### 3. Enter the virtual environment
```bash
pipenv shell
```
You should now see your shell prompt prefixed, indicating you are inside the environment.

### 4. Add your OpenAI API key
Create a `.env` file in the same directory as the code, with the following content:
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

- **LangChain LLM Chains:** Combines language models and prompt templates for multi-step reasoning and code/test generation.
- **Prompt Engineering:** Custom prompts to generate code and tests in your chosen language.
- **Conversational Memory:** Example scripts show persistent chat using LangChain memory components.
- **CLI Usage:** Run scripts with arguments for dynamic tasks.

---

## Project Usage Instructions

<!-- AUTO-GENERATED-LIST:START -->
### Files in Repository

- `.gitignore`
- `Resources/16-chains/code/.env`
- `Resources/16-chains/code/Pipfile`
- `Resources/16-chains/code/Pipfile.lock`
- `Resources/16-chains/code/main.py`
- `Resources/26-summarizations/chat/.env`
- `Resources/26-summarizations/chat/Pipfile`
- `Resources/26-summarizations/chat/Pipfile.lock`
- `Resources/26-summarizations/chat/main.py`
- `Resources/26-summarizations/chat/messages.json`
- `Resources/35-chunking/facts/.env`
- `Resources/35-chunking/facts/Pipfile`
- `Resources/35-chunking/facts/facts.txt`
- `Resources/35-chunking/facts/main.py`
- `Resources/37-introducing/facts/.env`
- `Resources/37-introducing/facts/Pipfile`
- `Resources/37-introducing/facts/emb/03d721ae-d724-4ee5-9aa9-61937c4be886/data_level0.bin`
- `Resources/37-introducing/facts/emb/03d721ae-d724-4ee5-9aa9-61937c4be886/header.bin`
- `Resources/37-introducing/facts/emb/03d721ae-d724-4ee5-9aa9-61937c4be886/length.bin`
- `Resources/37-introducing/facts/emb/03d721ae-d724-4ee5-9aa9-61937c4be886/link_lists.bin`
- `Resources/37-introducing/facts/emb/chroma.sqlite3`
- `Resources/37-introducing/facts/facts.txt`
- `Resources/37-introducing/facts/main.py`
- `Udemy_diagrams/01 - int.pdf`
- `Udemy_diagrams/02 - pycode.pdf`
- `Udemy_diagrams/03 - pycode.pdf`
- `Udemy_diagrams/04-tchat.pdf`
- `Udemy_diagrams/05-chain.pdf`
- `Udemy_diagrams/06-chain.pdf`
- `Udemy_diagrams/07-tchat.pdf`
- `Udemy_diagrams/07.1-tchat.pdf`
- `Udemy_diagrams/08-vectorstores.pdf`
- `Udemy_diagrams/09-agents.pdf`
- `Udemy_diagrams/10-app.pdf`
- `Udemy_diagrams/11-web.pdf`
- `Udemy_diagrams/12-app.pdf`
- `Udemy_diagrams/13-chat.pdf`
- `Udemy_diagrams/13-uploads.pdf`
- `Udemy_diagrams/14-int.pdf`
- `Udemy_diagrams/15-chat.pdf`
- `Udemy_diagrams/16-chat2.pdf`
- `Udemy_diagrams/17-chat3.pdf`
- `Udemy_diagrams/18-chat4.pdf`
- `Udemy_diagrams/19-chat5.pdf`
- `Udemy_diagrams/20-chat6.pdf`
- `Udemy_diagrams/21-chat7.pdf`
- `Udemy_diagrams/22-chat8.pdf`
- `Udemy_diagrams/23-chat9.pdf`
- `pycode/Pipfile`
- `pycode/Pipfile.lock`
- `pycode/facts/.env`
- `pycode/facts/Pipfile`
- `pycode/facts/Pipfile.lock`
- `pycode/facts/emb/82e1d589-8e2b-47cb-8363-6d20fd9b2544/data_level0.bin`
- `pycode/facts/emb/82e1d589-8e2b-47cb-8363-6d20fd9b2544/header.bin`
- `pycode/facts/emb/82e1d589-8e2b-47cb-8363-6d20fd9b2544/length.bin`
- `pycode/facts/emb/82e1d589-8e2b-47cb-8363-6d20fd9b2544/link_lists.bin`
- `pycode/facts/emb/chroma.sqlite3`
- `pycode/facts/facts.txt`
- `pycode/facts/main.py`
- `pycode/facts/prompt.py`
- `pycode/facts/redundant_filter_retriever.py`
- `pycode/main.py`
- `pycode/tchat/.env`
- `pycode/tchat/21-representing/chat/.env`
- `pycode/tchat/21-representing/chat/Pipfile`
- `pycode/tchat/21-representing/chat/Pipfile.lock`
- `pycode/tchat/21-representing/chat/main.py`
- `pycode/tchat/main.py`
- `pycode/tchat/messages.json`
- `scores.ipynb`
- `tools/git-daily`

### Sub-directory READMEs

- [pycode/README.md](pycode/README.md)
- [pycode/facts/README.md](pycode/facts/README.md)
- [pycode/tchat/README.md](pycode/tchat/README.md)
- [tools/README.md](tools/README.md)

<!-- AUTO-GENERATED-LIST:END -->
---

## Requirements

- Python 3.11
- Pipenv
- OpenAI account and API key

---

## Repo Structure

<!-- AUTO-GENERATED-LIST:START -->
- `pycode/main.py` – Sequential code & test generation
- `pycode/tchat/main.py` – Conversational chatbot using memory
- `facts/main.py` – Facts or trivia generation
- `Resources/16-chains/code/main.py` – Chained LLM example
<!-- AUTO-GENERATED-LIST:END -->
---

> **Note:** This is a course-following repo for learning and reference, not production-ready.

Owner: [alianwaar73](https://github.com/alianwaar73)

---

> _This README was generated and updated by GitHub Copilot AI._
