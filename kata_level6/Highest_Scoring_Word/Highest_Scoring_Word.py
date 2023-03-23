import string


def high(x):
    results = []
    alphabet = string.ascii_lowercase
    
    letter_points = {i: alphabet.index(i) + 1 for i in alphabet}
    
    x_list = x.split()
    for word in x_list:
        result_word = []
        for letter in word:
            result_word.append(letter_points[letter])
        results.append(sum(result_word))
    return x_list[results.index(max(results))]
