def nb_dig(n, d):
    list_of_sqr = []
    count = 0
    for i in range(0, n+1):
        list_of_sqr.append(str(i**2))
        for j in list_of_sqr[i]:
            if j == str(d):
                count += 1
    return count

