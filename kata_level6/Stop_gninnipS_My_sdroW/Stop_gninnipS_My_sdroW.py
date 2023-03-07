def spin_words(sentence):
    my_list = sentence.split()
    index = 0
    for i in my_list:
        if len(i) >= 5:
            my_list[index] = i[::-1]
        index += 1

    return " ".join(my_list)
