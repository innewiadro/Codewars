def capitals_first(text):
    words = text.split()
    upper = []
    lower = []
    for w in words:
        if not w[0].isalpha():
            continue
        if w[0].isupper():
            upper.append(w)
        else:
            lower.append(w)
    return " ".join(upper + lower)
