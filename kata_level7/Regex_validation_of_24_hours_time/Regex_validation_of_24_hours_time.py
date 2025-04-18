import re


def validate_time(time):
    pattern = r'^(?:[01]?\d|2[0-3]):[0-5]\d$'
    return re.fullmatch(pattern, time) is not None
