def pairs(ar):
    counter = 0

    for i in range(0, len(ar) - 1, 2):
        if abs(ar[i] - ar[i + 1]) == 1:
            counter += 1

    return counter
