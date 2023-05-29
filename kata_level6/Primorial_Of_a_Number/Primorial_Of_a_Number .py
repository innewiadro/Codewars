maxium = 10000
list_of_prime = []

for i in range(2, maxium + 1):
    if i > 1:  
        for j in range(2, i):  
            if (i % j) == 0:  
                break  
        else:  
            list_of_prime.append(i)


def num_primorial(n):
    number = 1
    for z in list_of_prime[:n]:
        number *= z
    return number
