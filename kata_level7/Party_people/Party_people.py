def party_people(lst):
    n = len(lst)

    freq = [0] * (n + 1)

    for x in lst:
        if x <= n:
            freq[x] += 1

    count = 0

    for k in range(n + 1):
        count += freq[k]
        if count == k:
            result = k

    return result if 'result' in locals() else 0
