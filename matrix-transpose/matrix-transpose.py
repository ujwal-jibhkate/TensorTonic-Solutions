import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    rows, cols = len(A), len(A[0])
    output_shape = (cols, rows)

    output = np.zeros(output_shape)

    for row in range(rows):
        for col in range(cols):
            output[col,row] = A[row][col]
    

    return output