def find_short(s):
    z = s.split(" ")
    L = []
    for word in z:
        L.append(len(word))
    L.sort()

    return int(L[:1][0])
