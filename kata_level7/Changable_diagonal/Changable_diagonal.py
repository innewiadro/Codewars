def matrix_diagonal(matrix, value):
    n = len(matrix)
    trace_sum = 0

    if value >= 0:
        for i in range(n - value):
            trace_sum += matrix[i + value][i]
    else:
        for i in range(n + value):
            trace_sum += matrix[i][i - value]

    return trace_sum
