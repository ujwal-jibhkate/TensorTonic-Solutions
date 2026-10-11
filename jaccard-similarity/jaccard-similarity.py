def jaccard_similarity(set_a: list, set_b: list) -> float:
    """
    Returns the Jaccard similarity of the two item collections.
    """
    # Write code here
    set_a = set(set_a)
    set_b = set(set_b)
    intersection = set_a & set_b
    union = set_a | set_b

    if len(union) == 0:
        return float(0)
        
    return float(len(intersection))/(len(union))

    