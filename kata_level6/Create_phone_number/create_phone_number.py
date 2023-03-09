def create_phone_number(n):
    return "("+"".join(str(e) for e in n[0:3]) + ") " + "".join(str(e) for e in n[3:6]) + "-"+"".join(str(e) for e in n[6:])
