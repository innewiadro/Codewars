def case_sensitive(s):
    not_lower = [char for char in s if char.isalpha() and not char.islower()]
    return [len(not_lower) == 0, not_lower]
