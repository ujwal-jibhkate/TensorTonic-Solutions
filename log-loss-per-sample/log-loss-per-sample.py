import math

def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) -> list:
    """
    Returns a list of loss values.
    """
    n =  len(y_true)
    result = []

    for i in range(n):
        y = y_true[i]
        probability =  y_pred[i]
        probability = max(eps, min(1 - eps, probability))
        result.append(-(y * math.log(probability) + (1 - y) * math.log(1 - probability)))
        
    return result