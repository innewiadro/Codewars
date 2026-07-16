def reverse_fun(strng: str) -> str:
    s = list(strng[::-1])

    for i in range(1, len(s)):
        s[i:] = reversed(s[i:])

    return ''.join(s)