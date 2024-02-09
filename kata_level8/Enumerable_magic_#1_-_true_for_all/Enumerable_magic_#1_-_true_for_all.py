def _all(seq, fun):
    if not seq:
        return True

    for item in seq:
        if not fun(item):
            return False

    return True
