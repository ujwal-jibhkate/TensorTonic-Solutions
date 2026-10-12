def percent_change(series: list) -> list:
    """
    Returns the fractional change between consecutive values.
    """
    # Write code here
    result = []
    
    for i in range(1, len(series)):
        if series[i-1] == 0:
            result.append(0)
        else:
            result.append((series[i]-series[i-1])/series[i-1])
        
    return result