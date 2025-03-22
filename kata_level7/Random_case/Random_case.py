from random import choice


def random_case(x):
    res = ''.join(map(choice, zip(x.lower(), x.upper())))
    return res
