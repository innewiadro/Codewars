def abbreviate(s):
    word = ''
    sentance = []
    abbreviation = []
    for i in s:
        if i.isalpha():
            word = word + i
        else:
            sentance.append(word)
            sentance.append(i)
            word = ''
    sentance.append(word)

    for word in sentance:
        length = len(word)
        if length > 3:
            a10n = word[0] + str(length - 2) + word[length - 1]
            abbreviation.append(a10n)

        else:
            abbreviation.append(word)

    return ''.join(abbreviation)
