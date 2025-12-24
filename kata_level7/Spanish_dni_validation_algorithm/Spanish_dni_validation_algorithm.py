def is_valid_dni(s: str) -> bool:
    if not isinstance(s, str) or len(s) != 9:
        return False

    if " " in s:
        return False

    number_part = s[:8]
    letter = s[8]

    if not number_part.isdigit():
        return False

    if not letter.isupper():
        return False

    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    expected_letter = letters[int(number_part) % 23]
    return letter == expected_letter
