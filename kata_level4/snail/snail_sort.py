def snail(snail_map):
    if snail_map == [[]]:
        return []

    else:
        size = len(snail_map)
        square = size * size
        row_length = size
        col_length = size
        mapa = []
        col_start = 0
        row_start = 0
        count_to_size = 0
        count_move = 0

        while True:

            for move_right in range(col_start, col_start + row_length):
                mapa.append(snail_map[col_start][move_right])
                count_move += 1
                count_to_size += 1
                if count_to_size == square:

                    return mapa
            col_start += (count_move - 1)
            row_start += 1
            col_length -= 1
            count_move = 0

            for move_down in range(row_start, row_start + col_length):

                mapa.append(snail_map[move_down][col_start])
                count_move += 1
                count_to_size += 1
                if count_to_size == square:
                    return mapa

            col_start -= 1
            row_start += (count_move - 1)
            row_length -= 1
            count_move = 0

            for move_left in range(col_start, col_start - row_length, -1):
                mapa.append(snail_map[row_start][move_left])
                count_move += 1
                count_to_size += 1
                if count_to_size == square:
                    return mapa

            col_start -= (count_move - 1)
            row_start -= 1
            col_length -= 1
            count_move = 0

            for move_up in range(row_start, row_start - col_length, -1):

                mapa.append(snail_map[move_up][col_start])
                count_move += 1
                count_to_size += 1
                if count_to_size == square:

                    return mapa

            col_start += 1
            row_start -= (count_move - 1)
            row_length -= 1
            count_move = 0
