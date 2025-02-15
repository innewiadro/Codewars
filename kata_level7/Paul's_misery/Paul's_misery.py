def paul(x):
    tab = {"kata": 5,
           'eating': 1,
           'Petes kata': 10,
           'life': 0}
    res = 0

    for i in x:
        if i in tab:
            res += tab[i]

    if res < 40:
        return "Super happy!"
    elif res <= 70:
        return "Happy!"
    elif res > 70 and res <= 100:
        return "Sad!"
    else:
        return "Miserable!"
