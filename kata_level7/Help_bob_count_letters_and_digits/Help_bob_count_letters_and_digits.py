import string


def count_letters_and_digits(s):
    alpha = string.ascii_lowercase + string.ascii_uppercase + "1234567890"
    res = 0
    for i in s:
        if i in alpha:
            res += 1
    return res
