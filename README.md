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

Below are brief instructions for running each project in this repository.

### 1. pycode

**Generate code and test:**
```bash
python pycode/main.py --language javascript --task 'print hello'
```
- This script uses LangChain and prompt engineering to generate code and corresponding tests in your chosen language.

### 2. tchat

**Start a conversational chat session:**
```bash
python pycode/tchat/main.py
```
- This launches a chatbot terminal session that uses LangChain's conversational memory for persistent chat.

### 3. facts

**Run the facts project:**
```bash
python facts/main.py
```
- This project provides facts or trivia (see the `facts` directory for more details). Make sure your `.env` file is set up if the script requires the OpenAI API key.

---

## Requirements

- Python 3.11
- Pipenv
- OpenAI account and API key

---

## Repo Structure

- `pycode/main.py` – Sequential code & test generation
- `pycode/tchat/main.py` – Conversational chatbot using memory
- `facts/main.py` – Facts or trivia generation
- `Resources/16-chains/code/main.py` – Chained LLM example

---

> **Note:** This is a course-following repo for learning and reference, not production-ready.

Owner: [alianwaar73](https://github.com/alianwaar73)

---

> _This README was generated and updated by GitHub Copilot AI._