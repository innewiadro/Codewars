import math


def iter_pi(epsilon):
    pi_approx = 0
    n = 0

    while True:
        term = (-1) ** n / (2 * n + 1)
        pi_approx += term
        current_pi = 4 * pi_approx

        if abs(current_pi - math.pi) < epsilon:
            return [n + 1, round(current_pi, 10)]

        n += 1