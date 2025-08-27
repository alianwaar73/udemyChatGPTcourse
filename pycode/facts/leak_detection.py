from __future__ import annotations

import re
from typing import Iterable, List, Tuple

try:
    # Optional import; types only where available
    from langchain.schema import Document  # type: ignore
except Exception:  # pragma: no cover - tests pass plain strings
    Document = object  # fallback type


_WORD_RE = re.compile(r"[A-Za-z0-9]+")


def _normalize(text: str) -> str:
    return " ".join(w.lower() for w in _WORD_RE.findall(text))


def _tokens(text: str) -> List[str]:
    return _normalize(text).split()


def _ngrams(tokens: List[str], n: int) -> List[Tuple[str, ...]]:
    if n <= 0:
        return []
    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]


def _join_docs(sources: Iterable) -> str:
    # Accept either LangChain Document objects or raw strings
    parts: List[str] = []
    for s in sources:
        if hasattr(s, "page_content"):
            parts.append(str(getattr(s, "page_content")))
        else:
            parts.append(str(s))
    return "\n".join(parts)


def coverage_score(answer: str, sources: Iterable, ngram: int = 2) -> float:
    """
    Returns fraction of answer n-grams found in sources text.

    - Uses word-level n-grams (default: bigrams) for robustness against single-word overlaps.
    - If the answer has fewer than `ngram` tokens, falls back to unigram coverage.
    """
    ans_tokens = _tokens(answer)
    src_tokens = _tokens(_join_docs(sources))

    if not ans_tokens:
        return 1.0

    if len(ans_tokens) < ngram:
        ngram = 1

    a_grams = _ngrams(ans_tokens, ngram)
    s_grams = set(_ngrams(src_tokens, ngram))

    if not a_grams:
        return 0.0

    hit = sum(1 for g in a_grams if g in s_grams)
    return hit / len(a_grams)


def detect_context_leak(answer: str, sources: Iterable, min_coverage: float = 0.5) -> Tuple[bool, float]:
    """
    Heuristic leak detector.

    - Computes bigram coverage of the answer against concatenated sources.
    - Flags a leak if coverage is below `min_coverage`.

    Returns: (is_leak, coverage)
    """
    cov = coverage_score(answer, sources, ngram=2)
    return (cov < min_coverage), cov


def coverage_report(answer: str, sources: Iterable, min_coverage: float = 0.5) -> str:
    leak, cov = detect_context_leak(answer, sources, min_coverage=min_coverage)
    status = "LEAK" if leak else "OK"
    return f"context-check: {status} (coverage={cov:.2f}, threshold={min_coverage:.2f})"

