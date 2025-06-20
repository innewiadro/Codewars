def sum_diagonals(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][i]
        total += matrix[i][n - 1 - i]
    return total
