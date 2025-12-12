def negation_value(s: str, val) -> bool:
    base = 0 if val in (None, []) else val
    return (len(s) + base) % 2 == 1
