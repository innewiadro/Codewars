def remove_bmw(string):
    if not isinstance(string, str):
        raise TypeError("This program only works for text.")

    forbidden = "BMWbmw"

    return "".join(ch for ch in string if ch not in forbidden)
