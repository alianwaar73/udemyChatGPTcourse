import pytest

from leak_detection import coverage_score, detect_context_leak, coverage_report


class DummyDoc:
    def __init__(self, text: str):
        self.page_content = text


def test_no_sources_is_leak():
    answer = "Mount Everest is the tallest mountain in the world."
    is_leak, cov = detect_context_leak(answer, [])
    assert is_leak is True
    assert cov == 0.0


def test_irrelevant_sources_is_leak():
    answer = "The Moon orbits the Earth approximately every 27 days."
    sources = [
        DummyDoc("The Sahara is the largest hot desert."),
        DummyDoc("Penguins live in the Southern Hemisphere."),
    ]
    is_leak, cov = detect_context_leak(answer, sources, min_coverage=0.4)
    assert is_leak is True
    assert cov < 0.4


def test_answer_supported_by_sources_not_leak():
    sources = [
        DummyDoc("Mars has the tallest volcano in the solar system, Olympus Mons."),
        DummyDoc("A day on Mars is called a sol and is just over 24 hours."),
    ]
    answer = "Mars has the tallest volcano in the solar system, Olympus Mons."
    is_leak, cov = detect_context_leak(answer, sources, min_coverage=0.5)
    assert is_leak is False
    assert cov >= 0.5


def test_short_answer_falls_back_to_unigrams():
    # Bigram coverage would be undefined for single-token answers; fallback should consider unigrams
    sources = [DummyDoc("Everest is the tallest mountain.")]
    answer = "Everest"
    cov = coverage_score(answer, sources, ngram=2)
    assert cov == 1.0


def test_report_format():
    sources = [DummyDoc("Zebras have black and white stripes.")]
    answer = "Zebras have stripes."
    text = coverage_report(answer, sources, min_coverage=0.3)
    assert text.startswith("context-check: ")

