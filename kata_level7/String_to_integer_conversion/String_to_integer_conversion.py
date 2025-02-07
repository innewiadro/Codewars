import re


def my_parse_int(strn):
    strn = strn.strip()
    if re.fullmatch(r"\d+", strn):
        return int(strn)

    return "NaN"
