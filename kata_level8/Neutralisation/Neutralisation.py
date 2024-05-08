def neutralise(s1, s2):
    strang = ""
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            strang += s1[i]
        else:
            strang += "0"
    return strang
