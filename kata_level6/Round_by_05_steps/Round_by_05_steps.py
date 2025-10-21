def solution(n):
    rest = 0
    if 0.75 > abs(n - int(n)) >= 0.25:
        rest = + 0.5
    elif 0.75 <= abs(n - int(n)):
        rest = + 1

    return int(n) + rest
