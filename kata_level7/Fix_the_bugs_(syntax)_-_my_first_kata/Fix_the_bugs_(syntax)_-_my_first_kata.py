def my_first_kata(a, b):
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        return False
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        return False
    if a == 0 or b == 0:
        return False
    return a % b + b % a