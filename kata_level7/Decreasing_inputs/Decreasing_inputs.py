def add(*args):
    result = 0
    n = 1
    for num in args:
        result += (num / n)
        n += 1
    return round(result)

