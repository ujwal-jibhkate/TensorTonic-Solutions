def exponential_moving_average(values: list, alpha: float) -> list:
    """
    Returns the exponential moving average at every position.
    """
    EMA = []

    EMA.append(values[0])

    for i in range(1, len(values)):
        ema = alpha * values[i] + (1 - alpha) * EMA[i-1]
        EMA.append(ema)

    return EMA