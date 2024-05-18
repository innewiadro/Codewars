def solution(pairs):
    res = ""
    for i, j in pairs.items():
        res += str(i) + " = " + str(j) + ","
    return res[:-1]
