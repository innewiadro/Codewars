def triple_x(s):
    first_x = s.find('x')
    if first_x == -1:
        return False
    return s[first_x:first_x + 3] == "xxx"
