def validate_pin(pin):
    for char in pin:
        if char not in "0123456789":
            return False

    if len(pin) == 4 or len(pin) == 6:
        return True
    else:
        return False
