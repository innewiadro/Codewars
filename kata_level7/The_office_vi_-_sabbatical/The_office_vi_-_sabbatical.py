def sabb(s, val, happiness):
    word = set("sabbatical")

    letter_count = sum(s.count(char) for char in word)

    total = val + happiness + letter_count

    if total > 22:
        return "Sabbatical! Boom!"
    else:
        return "Back to your desk, boy."
