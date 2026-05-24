from math import gcd
from functools import reduce
from collections import Counter

def has_subpattern(st):
    freq = Counter(st).values()
    return reduce(gcd, freq) > 1