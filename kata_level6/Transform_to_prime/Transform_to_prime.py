def minimum_number(numbers):
    def is_prime(n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    sum_to_prime = sum(numbers)
    additional_number = 0

    while not is_prime(sum_to_prime):
        sum_to_prime += 1
        additional_number += 1

    return additional_number

