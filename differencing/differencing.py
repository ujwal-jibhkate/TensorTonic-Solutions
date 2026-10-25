def differencing(series: list, order: int) -> list:
    """
    Returns the series after the requested differencing order.
    """
    for i in range(1, order+1):
        temp = []
        for j in range(len(series)-1):
            temp.append(series[j+1] - series[j])
        series = temp
    
    return temp