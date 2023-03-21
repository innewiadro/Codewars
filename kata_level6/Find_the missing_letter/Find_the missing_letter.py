def find_missing_letter(chars):
    if chars[0].isupper():
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    else:
        alpha = 'abcdefghijklmnopqrstuvwxyz'

    alpha_list = list(alpha)
    correct_list = alpha_list[alpha_list.index(chars[0]):alpha_list.index(chars[-1])]

    for i in correct_list:
        if i not in chars:
            return i
