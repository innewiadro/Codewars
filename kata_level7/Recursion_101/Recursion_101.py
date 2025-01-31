def solve(a, b):
    while a != 0 and b != 0:
        if a >= 2 * b:
            a %= 2 * b  # subtract as many multiples of 2*b as possible
        elif b >= 2 * a:
            b %= 2 * a  # subtract as many multiples of 2*a as possible
        else:
            break
    return [a, b]
