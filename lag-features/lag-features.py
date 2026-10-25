def lag_features(series: list, lags: list) -> list:
    """
    Returns the lag feature matrix.
    """
    lag = max(lags)
    result =[]

    for i in range(lag, len(series)):
        row = [series[i - lag] for lag in lags]
        result.append(row)
    
    return result