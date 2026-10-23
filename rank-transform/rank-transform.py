def rank_transform(values: list) -> list:
    """
    Returns the one-based average rank of every value.
    """
    n = len(values)
    indexed_values = sorted((val, idx) for idx, val in enumerate(values))
    
    ranks = [0.0] * n
    i = 0
    while i < n:
       
        j = i
        while j < n and indexed_values[j][0] == indexed_values[i][0]:
            j += 1
       
        avg_rank = (i + 1 + j) / 2.0
        
    
        for k in range(i, j):
            orig_idx = indexed_values[k][1]
            ranks[orig_idx] = avg_rank
            
        i = j  
    return ranks