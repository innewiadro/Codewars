def sq_in_rect(lng, wdth):
    if lng == wdth:
        return None
    list_of_squares = []
    area = lng * wdth
    while area > 0:
        if lng > wdth:
            list_of_squares.append(wdth)
            area -= wdth ** 2
            lng = lng - wdth
        else:
            list_of_squares.append(lng)
            area -= lng ** 2
            wdth = wdth - lng
    
    return list_of_squares 
