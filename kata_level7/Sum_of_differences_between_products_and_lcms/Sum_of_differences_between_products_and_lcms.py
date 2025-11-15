from math import gcd


def sum_differences_between_products_and_lmcs(pairs):
    total = 0
    for a, b in pairs:
        product = a * b

        if a == 0 or b == 0:
            lcm = 0
        else:
            lcm = product // gcd(a, b)

        total += product - lcm
    return total
