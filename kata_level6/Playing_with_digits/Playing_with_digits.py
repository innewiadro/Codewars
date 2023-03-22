def dig_pow(n, p):
    number = 0
    for i in range(0, len(str(n))):
        number += int(str(n)[i]) ** (p + i)

    return (number / n) if (number % n) == 0 else -1

