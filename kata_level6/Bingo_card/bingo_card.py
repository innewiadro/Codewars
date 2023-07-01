from random import randint


def get_bingo_card():
    bingo_list1 = ["B", "B", "B", "B", "B", "I", "I", "I", "I", "I", "N", "N", "N", "N", "G", "G", "G", "G", "G", "O",
                   "O", "O", "O", "O"]
    bingo_list = []
    
    while len(bingo_list) < 5:
        b = randint(1, 15)
        if b not in bingo_list:
            bingo_list.append(b)
            
    while len(bingo_list) < 10:
        i = randint(16, 30)
        if i not in bingo_list:
            bingo_list.append(i)
            
    while len(bingo_list) < 14:
        n = randint(31, 45)
        if n not in bingo_list:
            bingo_list.append(n)
            
    while len(bingo_list) < 19:
        g = randint(46, 60)
        if g not in bingo_list:
            bingo_list.append(g)
            
    while len(bingo_list) < 24:
        o = randint(61, 75)
        if o not in bingo_list:
            bingo_list.append(o)
    
    final_list = [i + str(j) for i, j in zip(bingo_list1, bingo_list)]
    
    return final_list
