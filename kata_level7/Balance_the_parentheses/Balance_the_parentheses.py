
def fix_parentheses(s) :
    open_needed = 0
    balance = 0

    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
            if balance < 0:
                open_needed += 1
                balance = 0

    return '(' * open_needed + s + ')' * balance
