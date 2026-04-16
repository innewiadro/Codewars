def change_me(m):
    d = {"£5":500,"£2":200,"£1":100,"50p":50,"20p":20}
    if m not in d: return m
    if m == "20p": return "10p 10p"
    a = d[m]
    return " ".join(["20p"]*(a//20) + ["10p"]*((a%20)//10))