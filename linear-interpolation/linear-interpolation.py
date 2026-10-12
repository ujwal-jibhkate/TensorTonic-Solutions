def linear_interpolation(values: list) -> list:
    """
    Returns a copy with every missing value interpolated.
    """
    # Write code here
    result = list(values)
    n = len(result)
    
    for i in range(n):
        if result[i] is None:
            
            left_idx = i - 1
            while left_idx >= 0 and result[left_idx] is None:
                left_idx -= 1

            right_idx = i + 1
            while right_idx <=n and result[right_idx] is None:
                right_idx += 1

            if left_idx >= 0 and right_idx < n:
                val_left = result[left_idx]
                val_right = values[right_idx]
                
                k = (i - left_idx) / (right_idx - left_idx)
                result[i] = val_left + k * (val_right - val_left)

    return result