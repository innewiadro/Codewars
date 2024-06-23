def arithmetic_sequence_elements(a, d, n):
    result = []
    for i in range(n):
        result.append(a + i * d)
    return ', '.join(map(str, result))
