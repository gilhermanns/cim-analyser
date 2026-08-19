from extract_kpis import extract_context


def test_extract_context_preserves_complete_words_at_window_boundaries():
    text = (
        "The company achieved a record $1.2 billion in revenue for the fiscal year. "
        "This represents a 20% increase year-over-year. Our Net Income (GAAP) was $150 million."
    )
    start = text.index("$150 million")
    end = start + len("$150 million")

    snippet = extract_context(text, start, end, radius=50)

    assert snippet.startswith("year-over-year")
    assert "Net Income (GAAP) was $150 million" in snippet
