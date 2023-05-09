def parse(data):
    a = 0
    lista = []
    for i in data:
        if i == 'i':
            a += 1 
        elif i == "d":
            a -= 1
        elif i == "s":
            a = a*a
        elif i == "o":
            lista.append(a)
            
    return lista
