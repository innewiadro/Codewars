def vowel_indices(word):
    index_list = []
    number = 1
    for i in word:
        if i in "aeiouyAEIOUY":
            index_list.append(number)
        number += 1

    return index_list
