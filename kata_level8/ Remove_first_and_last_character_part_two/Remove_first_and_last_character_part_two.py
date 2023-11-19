def array(string):
    numbers = string.split(",")
    numbers = numbers[1:-1]

    if len(numbers) == 0:
        return None

    return " ".join(string)
