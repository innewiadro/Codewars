def decode(code, key):
    key_digits = [int(d) for d in str(key)]
    key_length = len(key_digits)

    decoded_message = ''
    for i, num in enumerate(code):
        original_number = num - key_digits[i % key_length]

        decoded_message += chr(original_number + 96)

    return decoded_message
