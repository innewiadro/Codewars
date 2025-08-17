def title_to_number(title):
    a = 0
    n = 26

    for i in title:
        a = a * n + (ord(i) - ord('A') + 1)

    return a
