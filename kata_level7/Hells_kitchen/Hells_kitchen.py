def gordon(a):
    b = ""
    for i in a:
        if i in "euio":
            b += "*"
        else:
            b += i
    return "!!!! ".join(b.upper().replace("A", "@").split(" ")) + "!!!!"
