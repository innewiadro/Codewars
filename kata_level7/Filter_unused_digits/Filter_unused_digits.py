def missing_digits(*numbers):
    all_digits = set("0123456789")
    present_digits = set("".join(str(num) for num in numbers))
    missing = all_digits - present_digits
    return "".join(sorted(missing))
