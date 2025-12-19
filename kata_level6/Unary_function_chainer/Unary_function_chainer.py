from functools import reduce

def chained(functions):
    return lambda x: reduce(lambda acc, f: f(acc), functions, x)
