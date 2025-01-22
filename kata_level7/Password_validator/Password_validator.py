import re


def password(st):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return bool(re.match(pattern, st))
