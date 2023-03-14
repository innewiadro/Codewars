def to_camel_case(text):
    list_text = [letter for letter in text]
    for i in range(len(list_text)):
        if list_text[i] in ("_", "-"):
            list_text[i+1] = list_text[i+1].upper()
    return ''.join([i for i in list_text if i not in ('-', '_')])
