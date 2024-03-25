def to_csv_text(array):
    strings = ""
    for i in array:
        for j in i:
            strings += str(j) + ","
        strings = strings[:-1] + '\n'
    return strings[:-1]
