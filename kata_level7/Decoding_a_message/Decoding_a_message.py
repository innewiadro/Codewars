def decode(message):
    decoded = ''
    for char in message:
        if char.isalpha():
            decoded += chr(ord('a') + (25 - (ord(char) - ord('a'))))
        else:
            decoded += char
    return decoded
