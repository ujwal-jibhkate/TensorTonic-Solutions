def ordinal_encoding(values: list, ordering: list) -> list:
    """
    Returns the ordinal index of every input value.
    """
    ordinal = {}

    i = 0
    for order in ordering:
        ordinal[order] = i
        i += 1

    result = []
    for val in values:
        result.append(ordinal[val])

    return result