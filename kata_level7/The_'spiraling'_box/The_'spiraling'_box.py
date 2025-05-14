def create_box(m, n):  ## m and n positive integers
    result = [[0] * m for _ in range(n)]
    layers = (min(m, n) + 1) // 2

    for layer in range(layers):
        value = layer + 1
        for col in range(layer, m - layer):
            result[layer][col] = value
            result[n - 1 - layer][col] = value

        for row in range(layer, n - layer):
            result[row][layer] = value
            result[row][m - 1 - layer] = value

    return result
