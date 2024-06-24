def longest_word(string_of_words):
    words = string_of_words.split()
    max_length = 0
    longest = ""
    for word in words:
        if len(word) >= max_length:
            max_length = len(word)
            longest = word
    return longest
