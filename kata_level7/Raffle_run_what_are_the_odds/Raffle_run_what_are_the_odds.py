from math import gcd
from functools import reduce


def raffle_odds(totals, purchased):
    num = 1
    den = 1
    for t, p in zip(totals, purchased):
        num *= (t - p)
        den *= t

    win_num = den - num
    win_den = den

    g = gcd(win_num, win_den)
    return f"{win_num // g}/{win_den // g}"