def mean(lst):
    res = 0
    second = ""

    for i in lst:
        try:
            if isinstance(int(i), int):
                res += int(i)

        except:
            if isinstance(i, str):
                second += i

    first = res / 10

    return [first, second]
