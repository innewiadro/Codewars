def scale(strng, k, v):
    if not strng:
        return ""

    lines = strng.split('\n')

    scaled_lines = []

    for line in lines:
        horizontally_scaled = ''.join(char * k for char in line)

        for _ in range(v):
            scaled_lines.append(horizontally_scaled)

    return '\n'.join(scaled_lines)
