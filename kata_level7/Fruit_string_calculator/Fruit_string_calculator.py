import re


def calculate(text):
    numbers = re.findall(r'[0-9]+', text)
    numbers = [int(i) for i in numbers]
    if "loses" in text:
        res = numbers[0] - numbers[1]
    elif "gains" in text:
        res = sum(numbers)

    return res
