import numpy as np

def impute_missing(X: list, strategy: str = "mean") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as X.
    """
    data = np.asarray(X, dtype=float)
    print(data)

    if len(data.shape) == 1 :
      missing_mask = np.isnan(data)
      print(missing_mask)

      missing_entries = data[missing_mask]        
      observed_entries = data[~missing_mask]      
      
      if np.any(missing_mask) and len(observed_entries) > 0:
        if strategy == 'mean':
          fill_value = np.mean(observed_entries)
        elif strategy == 'median':
          fill_value = np.median(observed_entries)
        else:
          raise ValueError("Strategy must be 'mean' or 'median'")
            
        data[missing_mask] = fill_value
    else:
      for col_idx in range(data.shape[1]):
            col = data[:, col_idx]
            print(col)
            
            is_all_nan = np.isnan(col).all()
            
            missing_mask = np.isnan(col)
            observed_entries = col[~missing_mask]
              
            if is_all_nan:
                fill_value = 0  
            elif strategy == 'mean':
                fill_value = np.mean(observed_entries)
            elif strategy == 'median':
                fill_value = np.median(observed_entries)
            else:
                raise ValueError("Strategy must be 'mean' or 'median'")
                
            data[missing_mask, col_idx] = fill_value
            
        
    return data