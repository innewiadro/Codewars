def generate_hashtag(s):
    a = []
    list_of_words = s.split()
    
    for i in list_of_words:
        a.append(i.capitalize())
        
    b = "#" + "".join(a)
    
    return b if b != '#' and len(b) < 140 else False
