def calc_type(a, b, res):
    if a + b == res:
        return "addition"
    elif a - b == res:
        return "subtraction"
    elif a * b == res:
        return "multiplication"
    elif b != 0 and a / b == res:
        return "division"
