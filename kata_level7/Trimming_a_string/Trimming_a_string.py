def trim(phrase, size):
    if len(phrase) <= size:
        return phrase
    elif size <= 3:
        return phrase[:size] + "..."
    else:
        return phrase[:size - 3] + "..."
