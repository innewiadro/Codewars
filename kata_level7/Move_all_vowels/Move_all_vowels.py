def move_vowels(input):
    vowels = "aeiou"
    consonants = [char for char in input if char not in vowels]
    vowel_list = [char for char in input if char in vowels]
    return "".join(consonants + vowel_list)
