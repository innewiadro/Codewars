def check_vowel(s, n):
    return 0 <= n < len(s) and s[n].lower() in 'aeiou'
