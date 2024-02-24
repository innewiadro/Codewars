def product_fib(prod):
    fibo_num1 = 0
    fibo_num2 = 1
    value = 0
    counter = 0

    while value < prod:
        counter += 1
        fibo_num1 = fibonaci(counter)
        fibo_num2 = fibonaci(counter + 1)
        value = fibo_num1 * fibo_num2

    if value == prod:
        return [fibo_num1, fibo_num2, True]

    return [fibo_num1, fibo_num2, False]


def fibonaci(n):
    a = 1
    b = 1
    for i in range(n - 1):
        a, b = b, a + b

    return a
