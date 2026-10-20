def frequency_encoding(values: list) -> list:
    """
    Returns the relative frequency of every input value.
    """
    seen = {}
    result = []
    n = len(values)

    for val in values:
        if val in seen:
            seen[val] += 1
        else:
            seen[val] = 1

    for val in values:
        result.append(seen[val]/n)

    return result