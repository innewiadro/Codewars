def chess_board(rows, columns):
    board = []
    for i in range(rows):
        row = []
        
        for j in range(i, columns+i):
            if j % 2 != 0:
                row.append('X')
                    
            else:
                row.append('O')
        board.append(row)
        
    return board
