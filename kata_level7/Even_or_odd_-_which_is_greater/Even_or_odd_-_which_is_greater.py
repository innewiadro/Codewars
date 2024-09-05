def even_or_odd(s):
    even = 0
    odd = 0
    for i in s:
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)

    return 'Even and Odd are the same' if even == odd else "Even is greater than Odd" if even > odd else "Odd is greater than Even"
