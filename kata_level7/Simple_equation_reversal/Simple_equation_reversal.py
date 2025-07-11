import re


def solve(eq):
    tokens = re.findall(r'\w+|\S', eq)
    tokens.reverse()
    return ''.join(tokens)
