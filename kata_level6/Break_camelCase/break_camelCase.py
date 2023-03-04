import string


def solution(s):
    split = [s[0].lower()]

    big_alpha = string.ascii_uppercase
    for i in s[1:]:
        if i in big_alpha:
            split.append(" ")
            split.append(i.upper())
        else:
            split.append(i)
    return str.join("", split)
