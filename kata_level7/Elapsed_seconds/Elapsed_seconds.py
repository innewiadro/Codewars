import datetime


def elapsed_seconds(start, end):
    difference = end - start
    return difference.total_seconds()
