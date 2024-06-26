def solution(n):
    num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
               (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    roman_number = ""
    while n > 0:
        for i, r in num_map:
            while n >= i:
                roman_number += r
                n -= i
    return roman_number
