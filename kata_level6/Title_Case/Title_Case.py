def title_case(title, minor_words=''):
    lower_title = title.lower()
    lower_minor_words = minor_words.lower()
    title_list = lower_title.split()
    minor_words_list = lower_minor_words.split()
    new_title = []
    count = 0
    for i in title_list:
        if count == 0:
            new_title.append(i.capitalize())
            count += 1
            
        elif i not in minor_words_list:
            new_title.append(i.capitalize())
        else:
            new_title.append(i)
    return " ".join(new_title)
