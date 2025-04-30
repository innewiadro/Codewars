def validate_base(num, base):
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36 inclusive.")

    valid_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:base]
    numb = num.upper()

    return all(char in valid_chars for char in num)
