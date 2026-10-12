import numpy as np

def rotate_around_z(points: list, theta: float) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as points.
    """
    points = np.asarray(points)
    is_2d = points.ndim == 2

    if not is_2d:
        x , y , z = points[0], points[1], points[2]
        x_ = x * np.cos(theta) - y * np.sin(theta)
        y_ = x * np.sin(theta) + y * np.cos(theta)
        return np.asarray([x_, y_, z])
    else:
        result = []
        for point in points:
            x , y , z = point[0], point[1], point[2]
            x_ = x * np.cos(theta) - y * np.sin(theta)
            y_ = x * np.sin(theta) + y * np.cos(theta)
            result.append([x_, y_, z])
            
            
        return np.asarray(result)
        