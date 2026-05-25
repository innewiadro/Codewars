import re

def validate(message):
    pattern = r"^MDZHB \d{2} \d{3} [A-Z]+( \d{2}){4}$"
    return bool(re.match(pattern, message))