def geometric_sequence_elements(a, r, n):
    text = ""
    res = a
    for i in range(n-1):
        res = res * r
        text += str(res) + ", "
    return str(a) + ", " + text[:-2]
