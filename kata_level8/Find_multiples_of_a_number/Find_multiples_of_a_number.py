def find_multiples(integer, limit):
    a = []
    for i in range(1, limit+1):
        if i % integer == 0:
            a.append(i)
    return a
