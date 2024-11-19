def make_password(phrase):
    words = phrase.split()
    password = ''.join(word[0] for word in words)

    replacements = {'i': '1', 'I': '1', 'o': '0', 'O': '0', 's': '5', 'S': '5'}
    password = ''.join(replacements.get(char, char) for char in password)

    return password
