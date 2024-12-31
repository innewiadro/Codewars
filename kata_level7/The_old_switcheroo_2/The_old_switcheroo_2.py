def encode(st):
    result = []
    for char in st:
        if char.isalpha():
            result.append(str(ord(char.lower()) - 96))
        else:
            result.append(char)
    return ''.join(result)
