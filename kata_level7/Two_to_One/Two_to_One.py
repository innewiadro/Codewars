def longest(a1, a2):
    a = set(list(a1))
    a.update(list(a2))
    
    return "".join(sorted(a))
