def small_enough(array, limit):        
    a = [False for i in array if i > limit]
    return False if False in a else True
