import re

def validate_code(code):
    return bool(re.match(r'^[123]', str(code)))
