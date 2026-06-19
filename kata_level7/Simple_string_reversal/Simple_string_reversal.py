def solve(s):
    letters = [c for c in s if c != ' '][::-1]
    result = []
    letter_index = 0

    for char in s:
        if char == ' ':
            result.append(' ')
        else:
            result.append(letters[letter_index])
            letter_index += 1

    return ''.join(result)