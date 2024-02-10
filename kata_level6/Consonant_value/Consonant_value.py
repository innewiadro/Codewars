import re


def solve(s):
    alphabet = '-abcdefghijklmnopqrstuvwxyz'
    s = re.sub('[aeiou]+', ' ', s)
    s = s.split(" ")
    max_points = 0

    for element in s:
        total = 0
        for i in element:
            total += alphabet.index(i)

            if total > max_points:
                max_points = total

    return max_points
