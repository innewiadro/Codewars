def zipvalidate(postcode):
    if len(postcode) != 6:
        return False
    if not postcode.isdigit():
        return False
    if postcode[0] in {"0", "5", "7", "8", "9"}:
        return False
    return True
