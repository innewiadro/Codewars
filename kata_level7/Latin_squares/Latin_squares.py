def make_latin_square(n):
    square = [[0] * n for _ in range(n)]

    for i in range(n):
        square[0][i] = i + 1

    for row in range(1, n):
        for col in range(n):
            square[row][col] = square[row - 1][(col + 1) % n]

    return square
