def longest_consec(strarr, k):
    if not strarr or k > len(strarr) or k <= 0:
        return ""

    longest = ""
    for i in range(len(strarr) - k + 1):
        current = "".join(strarr[i:i + k])
        if len(current) > len(longest):
            longest = current

    return longest
