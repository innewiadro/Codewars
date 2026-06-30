from math import gcd

def som(x, y):
    return x + y

def mini(x, y):
    return min(x, y)

def maxi(x, y):
    return max(x, y)

def lcmu(x, y):
    x, y = abs(x), abs(y)
    return 0 if x == 0 or y == 0 else x * y // gcd(x, y)

def gcdi(x, y):
    return gcd(abs(x), abs(y))

def oper_array(fct, arr, init):
    result = []
    current = init

    for num in arr:
        current = fct(current, num)
        result.append(current)

    return result