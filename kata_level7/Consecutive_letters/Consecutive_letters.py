def solve(st):
    sorted_s = sorted(st)
    for i in range(1, len(sorted_s)):
        if ord(sorted_s[i]) != ord(sorted_s[i - 1]) + 1:
            return False

    return True
