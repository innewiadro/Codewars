def any_odd(x):
    odd_mask = 0xAAAAAAAA
    return (x & odd_mask) != 0
