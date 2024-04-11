def insert_dash(a):
    a = str(a)
    dashed = ''
    lastNum = a[len(a) - 1]

    for position in range(len(a) - 1):
        digit = int(a[position])
        nextDigit = int(a[position + 1])

        if digit % 2 != 0 and nextDigit % 2 != 0:
            dashed = dashed + str(digit) + '-'
        else:
            dashed = dashed + str(digit)

    return dashed + lastNum
