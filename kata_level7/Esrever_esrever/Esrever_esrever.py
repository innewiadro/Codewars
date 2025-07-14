def esrever(st):
    if not st:
        return st

    punctuation = st[-1]
    words = st[:-1].split()
    reversed_words = [word[::-1] for word in reversed(words)]
    return ' '.join(reversed_words) + punctuation
