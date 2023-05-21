def alternate(n, first_value, second_value):
    i = 0
    list_of_value = []
    while i < n:
        if i % 2 == 0:
            list_of_value.append(first_value)
            
        else:
            list_of_value.append(second_value)
        
        i+= 1
    
    return list_of_value
