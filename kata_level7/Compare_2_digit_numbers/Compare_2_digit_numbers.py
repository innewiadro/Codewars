def compare(a, b):
    a_to_list = list(str(a))  
    b_to_list = list(str(b))  
    count = 0
    
    for i in a_to_list:
        
        if i in b_to_list:
            count += 50
            b_to_list.remove(i)
    
    return f'{count}%'
