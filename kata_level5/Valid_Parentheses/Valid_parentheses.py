def valid_parentheses(string):
    new_string = ""
    counter = 0
    for i in string:
        if i == "(":
            new_string += i
            counter += 1
        elif i == ")":
            new_string += i
            counter -= 1

        if counter < 0:
            return False
    return True if counter == 0 else False
