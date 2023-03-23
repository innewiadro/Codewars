def century(year):
    return print(int(str(year / 100).split(".")[0]) + 1) if int(str(year)[-2:]) > 0 else print(int(str(year / 100).split(".")[0]))


def century1(year):
    return (year + 99) // 100
