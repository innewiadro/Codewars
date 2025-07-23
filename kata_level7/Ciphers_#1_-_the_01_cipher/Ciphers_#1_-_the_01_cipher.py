def encode(s):
    result = ''
    for char in s:
        if char.isalpha():
            index = ord(char.lower()) - ord('a')
            result += '1' if index % 2 else '0'
        else:
            result += char
    return result
