# pycode

This project is part of the [udemyChatGPTcourse](https://github.com/alianwaar73/udemyChatGPTcourse) repository and demonstrates how to use LangChain and OpenAI to automate code and test generation via prompt engineering and LLM chains.

---

## Environment Setup

This project uses **Python 3.11** and manages dependencies with [Pipenv](https://pipenv.pypa.io/en/latest/).

### 1. Install Pipenv (if not already installed)
```bash
pip install pipenv
```

### 2. Install dependencies and create environment
Run this in the `pycode/` directory (or the root where the `Pipfile` is present):
```bash
pipenv install
```

### 3. Enter the virtual environment
```bash
pipenv shell
```
You should now see your shell prompt prefixed, indicating you are inside the environment.

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

- **Automated Code Generation:** Uses LangChain and OpenAI to generate code snippets in your chosen language.
- **Automated Test Generation:** Immediately follows up by generating a test for the produced code.
- **Chained LLM Workflow:** Connects code and test generation in a sequential LLM chain.
- **Prompt Engineering:** Customizable code and test prompts.
- **Command Line Interface:** Easily specify the target language and coding task.

---

## Usage

In order to generate both code and a test for a specific task and language, run:

```bash
python main.py --language javascript --task "print hello"
```

- `--language`: Programming language for the generated code (default: python).
- `--task`: The function you want the code to perform.

Example output includes both the generated code and a test for it.

---

## File Structure

- `main.py` – Core script for code and test generation via LangChain and OpenAI.

---

## Requirements

- Python 3.11
- Pipenv
- OpenAI account and API key

---

> _This README was generated and updated by GitHub Copilot AI._
