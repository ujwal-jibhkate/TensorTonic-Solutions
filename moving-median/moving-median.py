def moving_median(values: list, window_size: int) -> list:
    """
    Returns the median of every complete sliding window.
    """

    def get_median(data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
    
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]
        
    result = []

    for i in range(len(values)-window_size+1):
        left = i
        right = i + window_size
        temp = values[left: right]
        result.append(float(get_median(temp)))

    return result