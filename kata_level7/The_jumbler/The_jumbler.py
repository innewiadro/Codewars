def jumbler(indices):
    arr = list(indices)
    steps = 0

    while indices[0] != 0:
        idx = indices[0]
        value = indices[idx]

        indices.pop(idx)
        indices.insert(0, value)

        steps += 1

    return steps