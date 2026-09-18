def rotate(matrix: list[list[int]]) -> None:
    """Rotate a square matrix 90 degrees clockwise in place."""
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("matrix must be square")
    for row in range(size):
        for column in range(row + 1, size):
            matrix[row][column], matrix[column][row] = (matrix[column][row], matrix[row][column])
    for row in matrix:
        row.reverse()
