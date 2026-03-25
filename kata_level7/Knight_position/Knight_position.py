def possible_positions(pos):
    col = ord(pos[0]) - ord('a')
    row = int(pos[1]) - 1

    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    result = []

    for dc, dr in moves:
        new_col = col + dc
        new_row = row + dr

        if 0 <= new_col < 8 and 0 <= new_row < 8:
            new_pos = chr(new_col + ord('a')) + str(new_row + 1)
            result.append(new_pos)

    return sorted(result)
