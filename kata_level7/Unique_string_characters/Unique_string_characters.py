def solve(a, b):
    new_str = ""
    for i in a:
        if i not in b:
            new_str += i

    for j in b:
        if j not in a:
            new_str += j
    return new_str
