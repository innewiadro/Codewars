def no_repeat(s):
    for char in s:
        if s.count(char) == 1:
            return char
