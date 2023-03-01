def open_or_senior(data):
    list_of_members = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            list_of_members.append("Senior")
        else:
            list_of_members.append("Open")

    return list_of_members
