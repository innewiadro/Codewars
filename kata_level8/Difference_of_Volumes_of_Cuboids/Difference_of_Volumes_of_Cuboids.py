def find_difference(a, b):
    a_cube = 1 
    b_cube = 1 
    for i in a:
        a_cube *= i
        
    for j in b:
        b_cube *= j
    
    return abs(a_cube - b_cube)
