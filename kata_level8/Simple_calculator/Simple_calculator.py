def calculator(x, y, op):
    print(x, y, op)
    if str(op) in "+-/*":
        try:
            result = eval(f'{x}{op}{y}')
        except:
            result = "unknown value"
    else:
        result = "unknown value"
    return result
