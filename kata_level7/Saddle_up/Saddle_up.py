def find_saddle_points(matrix):
    if not matrix:
        return []

    r = len(matrix)
    c = len(matrix[0])
    row_mins = [min(row) for row in matrix]
    col_maxs = [max(matrix[i][j] for i in range(r)) for j in range(c)]
    result = []
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == row_mins[i] and matrix[i][j] == col_maxs[j]:
                result.append((i, j))

    return result