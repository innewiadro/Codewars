def spoonerize(words):
    w1, w2 = words.split()
    return w2[0] + w1[1:] + " " + w1[0] + w2[1:]
