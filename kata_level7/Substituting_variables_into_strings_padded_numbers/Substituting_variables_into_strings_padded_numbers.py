def solution(value):
    new_value_as_str = "0" * (5 - len(str(value))) + str(value)
    return f"Value is {new_value_as_str}"
