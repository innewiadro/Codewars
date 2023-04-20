def remove(s):
    try:
        if s[-1] != '!':
            return s
        else:
            return s[:-1]
    except:
        return s
