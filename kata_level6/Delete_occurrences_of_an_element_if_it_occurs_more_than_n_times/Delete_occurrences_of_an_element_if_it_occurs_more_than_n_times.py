def delete_nth(order, max_e):
    my_dict = {}
    new_list = []
    for i in order:
        if i not in my_dict.keys():
             my_dict[i] = 1
                
        else:
            my_dict[i] += 1
            
        if my_dict[i] <= max_e:
            new_list.append(i)
            
    return new_list  
