def halving_sum(n):
    a=1
    res=0
    while n/a >= 1:
        res += n//a
        a=a*2
    return res
