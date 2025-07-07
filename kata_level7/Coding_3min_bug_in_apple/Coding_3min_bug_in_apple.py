def sc(apple):
    for x, row in enumerate(apple):
        for y, char in enumerate(row):
            if char == "B":
                return [x, y]