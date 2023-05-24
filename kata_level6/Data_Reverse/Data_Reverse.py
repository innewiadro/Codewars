def data_reverse(data):
    counter = 1
    big_list = []
    small_list = []
    for i in data:
        small_list.append(i)
        if counter % 8 == 0:
            big_list.append(small_list)
            small_list = []
        counter += 1
        
    return [i for sublist in big_list[::-1] for i in sublist]
