def baum_sweet():
    n = 0
    while True:
        if n == 0:
            yield 1
        else:
            b = bin(n)[2:]
            blocks = b.split('1')

            if all(len(block) % 2 == 0 for block in blocks):
                yield 1
            else:
                yield 0
        n += 1
