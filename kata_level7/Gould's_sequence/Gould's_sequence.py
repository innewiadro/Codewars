def gould():
    n = 0
    while True:
        yield n.bit_count()
        n += 1
