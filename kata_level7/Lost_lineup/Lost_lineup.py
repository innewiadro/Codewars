def find_lineup(distances):
    n = len(distances)
    order = [None] * n
    used_positions = set()

    for i, m in enumerate(distances):
        pos = m + 1

        if pos < 1 or pos > n:
            return []

        if pos in used_positions:
            return []

        used_positions.add(pos)
        order[pos - 1] = i + 1

    return order