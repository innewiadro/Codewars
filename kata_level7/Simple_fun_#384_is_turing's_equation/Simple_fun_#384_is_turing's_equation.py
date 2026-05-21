def is_turing_equation(s):
    left, result = s.split('=')
    a, b = left.split('+')

    a_rev = int(a[::-1])
    b_rev = int(b[::-1])
    c_rev = int(result[::-1])

    return a_rev + b_rev == c_rev