def calculator(equation):
    left, operator, right = equation.split()

    left_dots = len(left)
    right_dots = len(right)

    if operator == "+":
        result = left_dots + right_dots
    elif operator == "-":
        result = left_dots - right_dots
    elif operator == "*":
        result = left_dots * right_dots
    elif operator == "//":
        result = left_dots // right_dots

    return '.' * result
