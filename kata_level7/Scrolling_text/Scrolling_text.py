def scrolling_text(text):
    text = text.upper()
    new_list=[text]
    for i in range(len(text)):
        new_list.append(text[i+1:] + text[0:i+1])
    return new_list[:-1]
