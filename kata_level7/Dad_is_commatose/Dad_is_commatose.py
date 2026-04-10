import re


def dad_filter(string):
    string = re.sub(r',+', ',', string)
    string = re.sub(r'\s+,', ',', string)
    return string.rstrip(', ').strip()