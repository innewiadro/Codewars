def solve(string):
    lower = 0
    for i in string:
        if i.islower():
            lower = lower+1
    if lower >= 0.5*len(string):
        return string.lower()
    else:
        return string.upper()
