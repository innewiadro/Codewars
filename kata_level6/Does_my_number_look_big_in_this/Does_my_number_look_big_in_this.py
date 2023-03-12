def narcissistic(value):
    amount = 0
    for i in list(str(value)):
        amount += int(i) ** len(str(value))
    return amount == value
