def is_kiss(words):
    words = words.split()
    word_count = len(words)

    for w in words:
        if len(w) > word_count:
            return "Keep It Simple Stupid"

    return "Good work Joe!"
