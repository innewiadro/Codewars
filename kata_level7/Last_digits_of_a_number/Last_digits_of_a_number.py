def solution(n, d):
    res = [int(i) for i in list(str(n))]
    return res[-d:] if d > 0 else []
