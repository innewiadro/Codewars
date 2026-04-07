def binary_to_string(binary):
    parts = binary.split('0b')[1:]
    result = ''.join(chr(int(b, 2)) for b in parts)  
    return result
