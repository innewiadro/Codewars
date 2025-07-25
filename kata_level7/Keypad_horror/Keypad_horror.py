def computer_to_phone(numbers):
    mapping = {
        '7': '1', '8': '2', '9': '3',
        '4': '4', '5': '5', '6': '6',
        '1': '7', '2': '8', '3': '9',
        '0': '0'
    }
    return ''.join(mapping[digit] for digit in numbers)
