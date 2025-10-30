from collections import Counter


def most_common(s: str) -> str:
    freq = Counter(s)

    return ''.join(sorted(s, key=lambda c: -freq[c]))
