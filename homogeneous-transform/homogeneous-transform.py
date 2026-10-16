import numpy as np

def apply_homogeneous_transform(T: list, points: list) -> np.ndarray:
    """
    Returns transformed points with shape (3,) or (N, 3).
    """
    T = np.asarray(T, dtype=float)
    print("T :\n", T)
    print()
    points = np.asarray(points, dtype=float)   
    print("Points: ", points)
    single_point = points.ndim == 1
    print("single point: ", single_point)
    if single_point:
        points = points.reshape(1, 3)
        print("Reshaped points: \n", points)

    ones = np.ones((points.shape[0], 1))
    print("ones: ", ones)

    points_h = np.concatenate([points, ones], axis=1)
    print("P_h :", points_h)

    Transformed = (T@points_h.T).T[:, :3]

    return Transformed[0] if single_point else Transformed
