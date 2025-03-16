def word_to_bin(word):
    return ["0" + format(ord(x), 'b') for x in word]
