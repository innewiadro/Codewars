def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def strong_num(number):
    sum_of_factorials = sum(factorial(int(digit)) for digit in str(number))
    return "STRONG!!!!" if sum_of_factorials == number else "Not Strong !!"
