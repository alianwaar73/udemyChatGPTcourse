# facts

This project is part of the [udemyChatGPTcourse](https://github.com/alianwaar73/udemyChatGPTcourse) repository and demonstrates the use of LangChain and OpenAI for text chunking and processing, specifically for extracting and working with facts from a text file.

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

- **Text Loading & Chunking:** Loads facts from a plain text file (`facts.txt`) and splits the content into manageable "chunks" using custom settings.
- **Embeddings Preparation:** Prepares the text for further processing such as embeddings or advanced LLM tasks.
- **Customizable Chunking:** Uses LangChain's `CharacterTextSplitter` to control chunk size, separator, and overlap, allowing fine-tuned text handling.
- **Debugging Output:** Prints out each chunked text segment for inspection, ensuring chunking settings are appropriate for the document.

---

## Usage

To process the facts file and view chunked text segments, run:

```bash
python facts/main.py
```

You will see each chunked segment printed in the terminal, which can then be used for further LLM or embedding workflows.

---

## File Structure

- `main.py` – Loads, splits, and prints content from `facts.txt` using LangChain utilities.
- `facts.txt` – Text file containing facts to be processed (provide your own).

---

## Implementation Notes

This project, as explained in the code comments:
- Demonstrates the use of LangChain's `TextLoader` to load a text file.
- Uses `CharacterTextSplitter` to define how the text is divided (by newline, with a chunk size of 200 characters, and no overlap).
- Explains how chunking overlap is more relevant for longer documents (e.g. PDFs).
- Shows how to inspect chunked results for debugging and further development.

Review the comments in `main.py` for additional insights and learning.

---

## Requirements

- Python 3.11
- Pipenv
- OpenAI account and API key

---

> _This README was generated and updated by GitHub Copilot AI._