def exponential_moving_average(values: list, alpha: float) -> list:
    """
    Returns the exponential moving average at every position.
    """
    EMA = []
    EMA.append(values[0])
    rem =  1 - alpha

    for i in range(1, len(values)):
        EMA.append(alpha*values[i] + rem*EMA[i-1])

    return EMA