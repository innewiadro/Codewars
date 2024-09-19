def last_survivor(letters, coords):
    letters = list(letters)
    for index in coords:
        letters.pop(index)
    return letters[0]
