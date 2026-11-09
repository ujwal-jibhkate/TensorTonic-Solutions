def polynomial_features(values: list, degree: int) -> list:
    """
    Returns powers from zero through degree for every value.
    """
    result = []

    
    for val in values:
        temp =[1]
        for i in range(degree):
            temp.append(val**(i+1))
        result.append(temp)

    return result