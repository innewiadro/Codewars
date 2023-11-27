def correct(s):
    a = {"5": "S", "0": "O", "1": "I"}

    for i in s:
        if i in a:
            s = s.replace(i, a[i])

    return s
