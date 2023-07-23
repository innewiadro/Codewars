def divisible_by(numbers, divisor):
    a = []
    for i in numbers:
        if i % divisor == 0:
            a.append(i)
    return a
