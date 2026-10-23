def interaction_features(X: list) -> list:
    """
    Returns original features followed by unique pairwise products.
    """
    result = []

    for sample in X:
        expanded = list(sample)
        d = len(sample)

        for i in range(d):
            for j in range(i+1, d):
                expanded.append(sample[i] * sample[j])


        result.append(expanded)    

    return result