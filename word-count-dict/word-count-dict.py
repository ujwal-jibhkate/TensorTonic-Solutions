def word_count_dict(sentences: list) -> dict:
    """
    Returns a dictionary of token counts.
    """
    # Write code here
    seen = {}

    for sentence in sentences:
        for word in sentence:
            if word in seen:
                seen[word] +=  1
            else:
                seen[word] = 1

    return seen