def hydrate(drink_string):
    res = sum([int(x) for x in drink_string.split() if x.isnumeric()])
    return f"{res} glass of water" if res == 1 else f"{res} glasses of water"
