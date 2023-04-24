def pyramid(n):
    list_of_list = []
    if n > 0:
        for i in range(n):
            mid_list = []
            for j in range(i+1):
                mid_list.append(1)
            
            list_of_list.append(mid_list) 
    
    return list_of_list
        
