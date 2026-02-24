import re


def solve(s):
    numbers = re.findall(r'\d+', s)
    return max(map(int, numbers))
