def basic_op(operator, value1, value2):
    operations = {
        '+': value1 + value2,
        '-': value1 - value2,
        '*': value1 * value2,
        '/': value1 / value2,
    }
    return operations.get(operator)
