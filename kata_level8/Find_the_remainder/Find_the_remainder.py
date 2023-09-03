def remainder(a, b):
    return (a % b if a > b else b % a) if a and b != 0 else 0 if max(a,b) == 0 and min(a,b) < 0 else None