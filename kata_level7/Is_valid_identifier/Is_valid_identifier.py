import re


def is_valid(idn):
    return bool(re.fullmatch(r"[a-zA-Z_$][a-zA-Z0-9_$]*", idn))
