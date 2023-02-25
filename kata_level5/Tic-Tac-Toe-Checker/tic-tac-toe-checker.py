def is_solved(board):

    # rows
    for i in board:
        if i == [1, 1, 1]:
            return 1
        elif i == [2, 2, 2]:
            return 2
    # cols
    if (board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]) and board[1][1] != 0:
        if board[1][1] == 1:
            return 1
        elif board[1][1] == 2:
            return 2

    # diag
    elif (board[0][0] == board[1][0] == board[2][0]) and board[0][0] != 0:
        if board[0][0] == 1:

            return 1
        elif board[0][0] == 2:
            return 2
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != 0:
        if board[0][1] == 1:

            return 1
        elif board[0][1] == 2:

            return 2
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != 0:
        if board[0][2] == 1:

            return 1
        elif board[0][2] == 2:

            return 2

    # draw or not finished
    else:
        for i in board:
            for j in i:
                if j == 0:
                    return -1

        return 0
