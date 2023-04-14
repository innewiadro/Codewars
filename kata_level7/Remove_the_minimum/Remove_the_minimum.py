def remove_smallest(numbers):
    if len(numbers) < 1:
        return []
    b = min(numbers)
    new_numbers = numbers.copy()
    new_numbers.remove(b)
    return new_numbers
