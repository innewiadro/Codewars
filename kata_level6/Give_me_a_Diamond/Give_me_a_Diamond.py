def diamond(n):
    a = ''
    print(n)
    if n < 1 or not n % 2:
        return None
    
    for i in range(n):
        string = '*'*(i*2 + 1) if i <= n/2 else '*'*((n-i)*2 - 1)
        
        a += ' '*int((n-len(string)) / 2) + string + '\n'
    return a
