def shortcut(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [letter for letter in s if letter not in vowels]
    return ''.join(result)
