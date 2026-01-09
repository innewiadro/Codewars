def is_opposite(s1,s2):
    if not s1 and not s2:
        return False

    if len(s1) != len(s2):
        return False

    return all(a != b and a.lower() == b.lower() for a, b in zip(s1, s2))
