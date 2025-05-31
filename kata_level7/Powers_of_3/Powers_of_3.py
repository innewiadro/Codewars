def largest_power(N):
    if N <= 1:
        return -1
    k = 0
    while 3 ** (k + 1) < N:
        k += 1
    return k
