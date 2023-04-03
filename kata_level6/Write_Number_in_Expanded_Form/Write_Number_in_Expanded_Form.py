def expanded_form(num):
    a = []
    for i in range(1, len(str(num)) + 1):
        a.append(str(num % 10 ** i))
        num = num - num % 10 ** i
        if a[-1] == "0":
            a.pop()

    return " + ".join(a[::-1])

