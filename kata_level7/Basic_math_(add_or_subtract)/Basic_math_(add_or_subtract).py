def calculate(s):
    s1 = s.replace("plus", "+")
    s2 = s1.replace("minus", "-")
    return str(eval(s2))
