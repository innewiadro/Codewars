def get_the_vowels(word):
    vowels = "aeiou"
    count = 0
    expected = 0

    for ch in word:
        if ch == vowels[expected]:
            count += 1
            expected = (expected + 1) % len(vowels)

    return count
