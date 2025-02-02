def scramble(strng, array):
    new =[''] * len(strng)
    for i, j in zip(strng, array):
        new[j] = i
    return ''.join(new)
