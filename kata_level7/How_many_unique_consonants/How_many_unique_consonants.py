def count_consonants(text):
    vowels = "aeiou"
    consonants = set()

    for char in text.lower():
        if char.isalpha() and char not in vowels:
            consonants.add(char)

    return len(consonants)