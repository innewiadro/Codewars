import re


def to_cents(price: str):
    match = re.fullmatch(r'\$(\d+)\.(\d{2})', price)
    if match:
        dollars, cents = match.groups()
        return int(dollars) * 100 + int(cents)
    return None
