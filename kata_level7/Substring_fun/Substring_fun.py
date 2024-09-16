def nth_char(words):
    res= ""
    count = 0
    for j in words:
        res += j[count]
        count += 1
    return res
