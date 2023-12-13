def solve(s):
    upper, lower, numbers, special = 0, 0, 0, 0
    for i in s:
        if i.islower():
            lower += 1

        elif i.isupper():
            upper += 1

        elif i.isnumeric():
            numbers += 1

        else:
            special += 1

    return [upper, lower, numbers, special]
