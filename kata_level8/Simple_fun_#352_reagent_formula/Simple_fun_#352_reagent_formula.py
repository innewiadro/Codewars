def isValid(formula):
    formula_set = set(formula)

    if 1 in formula_set and 2 in formula_set:
        return False

    if 3 in formula_set and 4 in formula_set:
        return False

    if (5 in formula_set) != (6 in formula_set):
        return False

    if not (7 in formula_set or 8 in formula_set):
        return False

    return True
