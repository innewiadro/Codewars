def pattern(n):
    return '\n'.join('1' if i == 0 else "1" + i*'*' + str(i+1) for i in range(n))
