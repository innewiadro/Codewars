def quicksum(packet):
    if not packet:
        return 0

    if packet[0] == " " or packet[-1] == " ":
        return 0

    for char in packet:
        if not (char == " " or "A" <= char <= "Z"):
            return 0

    total = 0
    for i, char in enumerate(packet, start=1):
        if char != " ":
            value = ord(char) - ord('A') + 1
            total += i * value

    return total