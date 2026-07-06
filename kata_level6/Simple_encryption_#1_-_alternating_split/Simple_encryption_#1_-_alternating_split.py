
def encrypt(text, n):
    if not text or n <= 0:
        return text

    for _ in range(n):
        odd = text[1::2]
        even = text[0::2]
        text = odd + even

    return text


def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text

    for _ in range(n):
        mid = len(encrypted_text) // 2
        odd = encrypted_text[:mid]
        even = encrypted_text[mid:]

        result = []
        o = e = 0

        for i in range(len(encrypted_text)):
            if i % 2 == 0:
                result.append(even[e])
                e += 1
            else:
                result.append(odd[o])
                o += 1

        encrypted_text = "".join(result)

    return encrypted_text
