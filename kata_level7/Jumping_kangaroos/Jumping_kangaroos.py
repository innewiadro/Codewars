def kangaroo(kanga1, rate1, kanga2, rate2):
    if rate1 == rate2:
        return kanga1 == kanga2
    t = (kanga2 - kanga1) / (rate1 - rate2)
    return t.is_integer() and t >= 0
