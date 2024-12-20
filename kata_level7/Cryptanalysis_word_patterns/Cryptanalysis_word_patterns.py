def word_pattern(word):
    word = word.lower()

    char_to_index = {}

    pattern = []
    for i, char in enumerate(word):
        if char not in char_to_index:
            char_to_index[char] = len(char_to_index)
        pattern.append(str(char_to_index[char]))

    return ".".join(pattern)
