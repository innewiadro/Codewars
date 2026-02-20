def add(num1, num2):
    a = str(num1)
    b = str(num2)

    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ""

    for digit_a, digit_b in zip(a, b):
        result += str(int(digit_a) + int(digit_b))

    return int(result)