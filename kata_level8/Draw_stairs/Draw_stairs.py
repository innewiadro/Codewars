def draw_stairs(n):
    s = ''
    for i in range(n):
        s += " " * i + "I"+'\n'
    return s[:len(s)-1]
