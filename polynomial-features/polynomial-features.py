def polynomial_features(values: list, degree: int) -> list:
    """
    Returns powers from zero through degree for every value.
    """
    result = []

    
    for val in values:
        temp =[]
        for i in range(degree+1):
            temp.append(val**(i))
        result.append(temp)

    return result