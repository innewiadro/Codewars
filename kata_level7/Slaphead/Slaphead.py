def bald(s):
    count = s.count("/")
    cleaned_head = s.replace("/", "-")

    if count == 0:
        message = "Clean!"
    elif count == 1:
        message = "Unicorn!"
    elif count == 2:
        message = "Homer!"
    elif 3 <= count <= 5:
        message = "Careless!"
    else:
        message = "Hobo!"

    return [cleaned_head, message]
