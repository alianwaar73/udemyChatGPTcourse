# facts

This project is a follow-up to an online course (not suitable for production scenarios) and demonstrates the use of LangChain, OpenAI, and ChromaDB for processing, embedding, and querying textual facts. It is part of the [udemyChatGPTcourse](https://github.com/alianwaar73/udemyChatGPTcourse) repository.

---

## Overview

The project showcases:

- **Loading and Chunking Text:** Facts are loaded from a simple text file and split into manageable chunks.
- **Embeddings and Vector Store:** Each chunk is embedded using OpenAI's embeddings and stored in a Chroma vector database.
- **Prompting and Retrieval:** The system allows querying the stored facts using a prompt, leveraging retrieval-augmented generation (RAG) pipelines.
- **Redundancy Filtering:** Custom retrieval logic is implemented to remove duplicate/redundant documents from query results using embedding similarity.

---

## Environment Setup

This project uses **Python 3.11** and manages dependencies via [Pipenv](https://pipenv.pypa.io/en/latest/).

1. **Install Pipenv:**
   ```bash
   pip install pipenv
   ```

2. **Install dependencies:**
   ```bash
   pipenv install
   ```

3. **Activate the virtual environment:**
   ```bash
   pipenv shell
   ```

4. **Add your OpenAI API key:**
   Create a `.env` file in this directory with:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

5. **Exit the environment:**
   ```bash
   exit
   ```

---

## File Structure

- `facts.txt` – List of facts to be processed.
- `main.py` – Loads, splits, embeds facts, and stores them in ChromaDB. Also demonstrates querying the vector db.
- `prompt.py` – Enables interactive querying of the embedded facts using a RetrievalQA chain, utilizing a custom retriever to filter redundant results.
- `redundant_filter_retriever.py` – Custom retriever class to filter out redundant/duplicate documents based on embedding similarity.
- `Pipfile` – Dependency management.

---

## Usage

### 1. **Embedding & Storing Facts**

Run the main script to load facts, split them, generate embeddings, and store them in ChromaDB:

```bash
python main.py
```

This will print out the most relevant facts for a sample query.

> **Note:**  
> Each time you run `main.py`, embeddings are recalculated and stored in ChromaDB, which may incur OpenAI API costs. In a production setup, embedding calculation and storage should be decoupled to avoid redundant computation and extra costs.

### 2. **Querying the Facts**

Once embeddings are stored, you can interactively query the facts using:

```bash
python prompt.py
```

This script uses a chain with a chat model and retrieves relevant facts from the vector store, demonstrating retrieval-augmented QA with redundancy filtering.

---

## Key Concepts & Implementation Details

### Text Chunking & Embeddings

- Facts are loaded using `TextLoader`.
- Chunking is done by `CharacterTextSplitter` using a newline (`\n`) separator, chunk size of 200 characters, and zero overlap. This is optimal for short .txt files, but for larger documents (e.g. PDFs), overlap settings become more important to avoid abrupt splits.
- Embeddings are generated using OpenAI's embedding model.

### Vector Store & Cost Considerations

- The vector store uses ChromaDB for efficient similarity search.
- - [ ] How much does this cost?
  - [x] Addressed: The cost depends on the number and size of embeddings generated, as OpenAI charges per token. For small .txt files, the cost is minimal, but for larger datasets, cost analysis is recommended. For large-scale use, monitor API usage and decouple embedding generation from querying to optimize costs.
- Embeddings and vector store are persistently stored in the `emb/` directory.

### Redundancy Filtering

- `redundant_filter_retriever.py` introduces a custom retriever (`RedundantFilterRetriever`) that filters out duplicate or highly similar documents in retrieval, using the `max_marginal_relevance_search_by_vector` method.
- The lambda parameter (`lambda_mult=0.8`) controls the allowed repetitiveness; higher values allow more similarity.

### Prompting & Query Chains

- `prompt.py` demonstrates using a RetrievalQA chain with a chat model and the custom retriever to answer natural language queries based on the stored facts.
- - [ ] Slightly confused with the following line. Are we recalculating the embeddings here? If so then why? Shouldn't we just be accessing it somehow?
  - [x] Addressed: The embedding function is required so the system can embed your query for similarity search, but unless you add new documents, the document embeddings stored in ChromaDB are not recalculated—only the query is embedded at retrieval time.
- The code comments discuss confusion regarding embedding recalculation—ChromaDB requires an embedding function for similarity search, but embeddings themselves are only recalculated if new documents are added.

---

## Comments & To-Do Summaries

The following are summaries of code comments marked as todo comments (noted in code with [ ]). Each has been addressed here using the standard README markup syntax:

- [ ] How much does this cost?  
  - [x] Addressed above in Key Concepts: Cost is minimal for small files, but should be monitored for larger datasets.
- [ ] Slightly confused with the following line. Are we recalculating the embeddings here?  
  - [x] Clarified above in Prompting & Query Chains: Only query embeddings are recalculated, not document embeddings.
- [ ] The following block of code is customary to include. For the purposes of this project the above block suffices.  
  - [x] The async method stub is included for completeness but is not used here.

All todo comments from code files have been summarized and addressed in the most context-appropriate section of this README.

---

## Limitations

- This codebase is for educational use and not production-ready.  
- Embedding and storage should be separated in real-world scenarios to avoid unnecessary API usage and costs.
- The redundancy filter retriever can be fine-tuned for more sophisticated duplicate detection as needed.

---

## Requirements

- Python 3.11
- Pipenv
- OpenAI account and API key

---

> _This README was generated and updated using Copilot's AI. All todo comments in code files have been summarized, addressed, and clarified per project instructions._