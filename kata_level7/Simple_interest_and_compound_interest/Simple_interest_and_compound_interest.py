def interest(p, r, n):
    simple = p * (1 + r * n)
    compound = p * (1 + r) ** n
    return [round(simple), round(compound)]