def missing(indexes, comment):
    cleaned = comment.replace(" ", "")
    indexes = sorted(indexes)
    if any(i >= len(cleaned) for i in indexes):
        return "No mission today"
    word = ''.join(cleaned[i] for i in indexes).lower()
    return word
