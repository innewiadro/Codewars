def eliminate_unset_bits(number):
    filtered_binary = number.replace('0', '')
    return int(filtered_binary, 2) if filtered_binary else 0
