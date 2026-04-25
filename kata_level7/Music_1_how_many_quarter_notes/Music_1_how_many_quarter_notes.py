def find_quarter_notes(time_signature):
    a, b = map(int, time_signature.split('/'))

    if b <= 0 or (b & (b - 1)) != 0:
        return None

    result = (4 * a) // b

    return result if result >= 1 else 0