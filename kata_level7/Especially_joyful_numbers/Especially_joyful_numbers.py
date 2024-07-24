def number_joy(n):
    res = 0
    for i in str(n):
        res += int(i)

    return res * int(str(res)[::-1]) == n
