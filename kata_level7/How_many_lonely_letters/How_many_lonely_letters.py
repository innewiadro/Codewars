import string
from collections import Counter


def count_lonely_letters(text):
    filtered = [c.lower() for c in text if c.isalpha()]

    counts = Counter(filtered)
    alphabet = string.ascii_lowercase

    lonely_count = 0

    for letter in counts:
        if counts[letter] != 1:
            continue

        idx = alphabet.index(letter)

        prev_letter = alphabet[idx - 1] if idx > 0 else None
        next_letter = alphabet[idx + 1] if idx < 25 else None

        if ((prev_letter is None or counts[prev_letter] == 0) and
                (next_letter is None or counts[next_letter] == 0)):
            lonely_count += 1

    return lonely_count