def to_acronym(inp):
    res=""
    for i in range(len(inp.split(" "))):
        res += inp.split(" ")[i][0].upper()
    return res
