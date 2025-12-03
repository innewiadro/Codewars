def extract_bits(field: int, offset: int, length: int):
    field &= (1 << 64) - 1

    if length == 0 or offset >= 64:
        return 0

    shifted = field >> offset
    mask = (1 << length) - 1

    return shifted & mask
