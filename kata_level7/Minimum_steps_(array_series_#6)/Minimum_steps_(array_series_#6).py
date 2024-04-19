def minimum_steps(numbers, value):
    print(numbers, value)
    a = sorted(numbers)
    couter = 0
    suma = 0
    for i in a:
        suma += i
        if suma >= value:
            return couter
        else:
            couter += 1
