# udemyChatGPTcourse

First go through of Udemy's ChatGPT course. Lightly commented. No personal projects. [Course link](https://www.udemy.com/share/109HbI3@2jeNzCrmSShzOCAt5UMVGp3QlEZwnffD5prYbjKQYgFIqwTksjdNRUU72UkRRxdk5g==/). Course author: [Stephen Grider](https://github.com/StephenGrider) 

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

## Example Usage

Generate code and test:
```bash
python pycode/main.py --language javascript --task 'print hello'
```

Start a chat session:
```bash
python pycode/tchat/main.py
```

---

## Requirements

- Python 3.11
- Pipenv
- OpenAI account and API key

---

## Repo Structure

- `pycode/main.py` – Sequential code & test generation
- `pycode/tchat/main.py` – Conversational chatbot using memory
- `Resources/16-chains/code/main.py` – Chained LLM example

---

> **Note:** This is a course-following repo for learning and reference, not production-ready.

Owner: [alianwaar73](https://github.com/alianwaar73)
