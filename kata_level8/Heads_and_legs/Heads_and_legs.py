def animals(heads, legs):
    if heads < 0 or legs < 0:
        return "No solutions"

    elif heads == 0 and legs == 0:
        return 0, 0

    cow = (legs - 2 * heads) / 2
    czik = heads - cow

    if not czik.is_integer() or not cow.is_integer():
        return "No solutions"
    elif czik >= 0 and cow >= 0:
        return czik, cow
    else:
        return "No solutions"
