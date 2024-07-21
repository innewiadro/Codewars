def move_ten(s):
    shifted = []
    for char in s:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + 10) % 26 + ord('a'))
            shifted.append(new_char)
        elif 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + 10) % 26 + ord('A'))
            shifted.append(new_char)
        else:
            shifted.append(char)
    return ''.join(shifted)
