def scrabble_score(word):
    return sum(dict_scores.get(letter.upper(), 0) for letter in word)
