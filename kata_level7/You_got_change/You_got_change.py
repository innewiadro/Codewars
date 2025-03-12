def give_change(amount):
    numbers = [1, 5, 10, 20, 50, 100]
    number_counts = [0] * len(numbers)

    for i in range(len(numbers) - 1, -1, -1):
        number_counts[i] = amount // numbers[i]
        amount %= numbers[i]

    return tuple(number_counts)
