def is_divisible(*numbers):
    first = numbers[0]
    for num in numbers[1:]:
        if first % num != 0:
            return False
    return True
