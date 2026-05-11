def is_same_language(lst): 
    first_language = lst[0]['language']
    return all(dev['language'] == first_language for dev in lst)