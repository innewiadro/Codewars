def tricky_doubles(num):
    s = str(num)
    m = len(s)

    if m % 2 == 0 and s[:m // 2] == s[m // 2:]:
        return num

    return num * 2
