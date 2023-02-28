def get_count(sentence):
    num_vowels = 0
    for char in sentence:
        if char in "aeiouAEIOU":
            num_vowels = num_vowels+ 1
    return num_vowels
