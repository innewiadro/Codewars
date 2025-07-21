import math


def square_pi(digits):
    pi_digits = '31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
    selected_digits = pi_digits[:digits]
    total = sum(int(d)**2 for d in selected_digits)
    return math.ceil(math.sqrt(total))
