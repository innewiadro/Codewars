def dative(word):
    front_vowels = {'e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű'}
    back_vowels = {'a', 'á', 'o', 'ó', 'u', 'ú'}

    for char in reversed(word):
        if char in front_vowels:
            return word + 'nek'
        if char in back_vowels:
            return word + 'nak'
    return word