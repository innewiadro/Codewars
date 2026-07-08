def kooka_counter(laughing):
    if not laughing:
        return 0

    count = 1

    for i in range(2, len(laughing), 2):
        if laughing[i].isupper() != laughing[i - 2].isupper():
            count += 1

    return count