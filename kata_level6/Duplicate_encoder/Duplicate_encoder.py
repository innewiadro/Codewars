def duplicate_encode(word):
    string = ''
    word_lower = word.lower()
    amount = {i: 0 for i in word_lower}

    for i in word_lower:
        amount[i] = amount.get(i) + 1

    for i in word_lower:
        if amount[i] > 1:
            string += ')'
        else:
            string += '('
    return string
