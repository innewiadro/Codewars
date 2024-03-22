def encode(message, key):
    code = []
    res = [int(x) for x in str(key)]
    number = 0
    for i in message:
        code.append(ord(i) - 96 + res[number % len(str(key))])
        number += 1
    return code
