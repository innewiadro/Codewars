def count_sheep(n):
    string = ""
    if n > 0:
        for i in range(1, n+1):
            string += f'{i} sheep...'
    return string
