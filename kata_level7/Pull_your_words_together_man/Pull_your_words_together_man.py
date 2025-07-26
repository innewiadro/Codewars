def sentencify(words):
    if not words:
        return ""
    sentence = ' '.join(words)
    return sentence[0].upper() + sentence[1:] + '.'
