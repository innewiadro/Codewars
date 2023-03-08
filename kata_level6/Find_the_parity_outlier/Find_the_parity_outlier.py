def find_outlier(integers):
    add = 0
    
    for i in integers[0:3]:
        if i % 2 == 0:
            add += 1

    for i in integers:
        if add < 2 and i % 2 == 0:
            return i
        elif add >= 2 and i % 2 !=0:

            return i
