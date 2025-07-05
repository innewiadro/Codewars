import re


def i_before_e(word):
    def reorder(match):
        seq = match.group()
        prev_char = match.start() - 1
        preceding_c = word[prev_char] == 'c' if prev_char >= 0 else False

        i_count = seq.count('i')
        e_count = seq.count('e')

        if preceding_c:
            return 'e' * e_count + 'i' * i_count
        else:
            return 'i' * i_count + 'e' * e_count

    return re.sub(r'[ie]+', reorder, word)
