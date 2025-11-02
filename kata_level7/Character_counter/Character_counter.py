def validate_word(word):
    word = word.lower()
    counts = [word.count(ch) for ch in set(word)]
    return len(set(counts)) == 1
