def multiplication_table(size):
    big_list = []
    small_list = []
    j = 1
    for i in range(1, size + 1):
        for i in range(1, size + 1):
            small_list.append(i*j)
        
        j += 1
        big_list.append(small_list)
        small_list = []
    return big_list
