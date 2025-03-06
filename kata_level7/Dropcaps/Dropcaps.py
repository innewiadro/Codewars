def drop_cap(s):
    return " ".join(word.capitalize() if len(word) > 2 else word for word in s.split(" "))
