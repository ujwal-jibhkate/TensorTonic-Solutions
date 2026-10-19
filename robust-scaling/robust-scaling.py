def robust_scaling(values: list) -> list:
    """
    Returns values centered by the median and scaled by the interquartile range.
    """
    def find_median(sub_list):
      n = len(sub_list)
      mid = n // 2
      if n % 2 == 0:
        return (sub_list[mid - 1] + sub_list[mid]) / 2.0
      else:
        return sub_list[mid]

    sorted_data = sorted(values)
    n = len(values)

    if n==1:
        return [ 0 ]

    if n % 2 == 0:
      lower_half = sorted_data[:n // 2]
      upper_half = sorted_data[n // 2 :]
    else:
      lower_half = sorted_data[: n // 2]
      upper_half = sorted_data[(n // 2) + 1 :]
      
    q1 = find_median(lower_half)
    q2 = find_median(sorted_data)
    q3 = find_median(upper_half)

    IQR = q3 - q1

    if IQR == 0:
        IQR = 1.0

    result = []

    for val in values:
      result.append((val - q2)/IQR)

    return result