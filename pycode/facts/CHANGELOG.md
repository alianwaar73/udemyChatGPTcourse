# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog, and this project adheres to Semantic Versioning where practical for this submodule.

## [0.2.0] - 2025-08-26

### Added
- Interactive REPL (`repl.py`) to query facts with a friendly prompt.
  - Startup scope banner: shows `facts.txt` path, rough count, last modified time, topic hints, and vector store status.
  - Commands: `:help`, `:scope`, `:sources`, `:rebuild`, `:clear`, `:exit`.
  - Optional index creation in `emb/` with clear API cost notice.
- Out-of-scope handling in REPL:
  - Strict mode (`:strict`) with similarity score threshold and abstention prompt.
  - Pre-flight retrieval gate: if no relevant docs, skip LLM and return out-of-scope message.
  - Controls: `:topk <n>`, `:thresh <0-1>`.
- Documentation updates in `README.md` for REPL usage and behavior.

### Changed
- `prompt.py` now notes `repl.py` as the preferred interactive entry point.
 - `redundant_filter_retriever.py` now supports configurable `k` to control MMR results.

### Notes
- REPL uses existing `redundant_filter_retriever.py` to reduce redundancy in results.
- Embeddings are persisted in `emb/`; only query embeddings are computed at retrieval time unless rebuilding the index.

## [0.1.0] - 2024-06-05

### Added
- Initial version: load, split, embed facts, and store in Chroma (`main.py`).
- Custom `RedundantFilterRetriever` and example `prompt.py` for retrieval-augmented QA.
