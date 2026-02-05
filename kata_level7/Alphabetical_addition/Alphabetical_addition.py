def add_letters(*letters):
    if not letters:
        return 'z'

    total = sum(ord(letter) - 96 for letter in letters)

    result_position = total % 26

    if result_position == 0:
        return 'z'

    return chr(result_position + 96)
