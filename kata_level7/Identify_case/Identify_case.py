def case_id(s):
    if "-" in s:
        if "_" in s:
            return "none"
        parts = s.split("-")
        if all(part.islower() and part for part in parts):
            return "kebab"
        return "none"

    if "_" in s:
        parts = s.split("_")
        if all(part.islower() and part for part in parts):
            return "snake"
        return "none"

    if s[0].islower() and any(c.isupper() for c in s):
        if s.isalpha():
            return "camel"

    return "none"