from functools import reduce


def process_data(data):
    processed = [x - y for x, y in data]
    return reduce(lambda a, b: a * b, processed)
