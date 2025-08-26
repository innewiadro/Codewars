def clonewars(k):
    total_kata = 0
    for n in range(1, k+1):
        total_kata += (2**(n-1)) * (k - (n-1))
    return [2**(k-1), total_kata] if total_kata> 0 else [1, 0]
