def remove(string):
    words = string.split(" ")
    cleaned_words = [word.rstrip('!') for word in words]

    return " ".join(cleaned_words)