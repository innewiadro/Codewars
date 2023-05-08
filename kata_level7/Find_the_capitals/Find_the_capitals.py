def capitals(word):
    capital = []
    count = 0
    for i in word:
        if i.isupper():
            capital.append(count)
        count += 1
    return capital
