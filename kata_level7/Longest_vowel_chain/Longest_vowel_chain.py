def solve(s):
    vowel_len = 0
    max_chain = 0
    for i in s:

        if i in "aeiou":
            vowel_len += 1
        else:
            vowel_len = 0

        if max_chain < vowel_len:
            max_chain = vowel_len

    return max_chain
