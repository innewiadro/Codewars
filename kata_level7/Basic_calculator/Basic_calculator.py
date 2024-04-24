def calculate(num1, operation, num2):
    if operation == "+":
        return num1 + num2

    if operation == "-":
        return num1 - num2

    if operation == "/":
        return num1 / num2 if num2 != 0 else None

    if operation == "*":
        return num1 * num2

    else:
        return None
