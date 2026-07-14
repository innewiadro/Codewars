def reverse_message(text):
    if not text:
        return ""

    result = []
    for word in text.split():
        rev = word[::-1].lower()
        if rev and rev[0].isalpha():
            rev = rev[0].upper() + rev[1:]
        result.append(rev)

    return " ".join(result[::-1])
