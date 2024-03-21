def bingo(ticket,win):
    minwin = 0
    for i in ticket:
        for j in i[0]:
            if ord(j) == i[1]:
                minwin += 1
    return 'Winner!' if minwin >= win else 'Loser!'
