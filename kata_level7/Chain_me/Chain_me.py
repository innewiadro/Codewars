def chain(init_val, functions):

    result = init_val
    for func in functions:
        result = func(result)
    return result


def add10(x):
    return x + 10

def mul30(x):
    return x * 30
