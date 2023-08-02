def solve(n):
    if n % 10 != 0:
        return -1
    number_of_banknotes = 0
    values = [500, 200, 100, 50, 20, 10]
    for i in values:
        b = n // i 
        if b > 0:
            n -= i * (b)
            number_of_banknotes += b
    return number_of_banknotes
