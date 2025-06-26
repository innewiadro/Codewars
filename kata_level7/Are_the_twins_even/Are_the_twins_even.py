def even_twins(arr):
    even_sums = set()
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            s = arr[i] + arr[j]
            if s % 2 == 0:
                even_sums.add(s)
    return len(even_sums)
