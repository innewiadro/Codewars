def remove(s):
    words = s.split()
    result = []
    for word in words:
        if word.count('!') != 1:
            result.append(word)

    return " ".join(result)
