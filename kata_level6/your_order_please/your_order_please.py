def order(sentence):
    numbers = "123456789"
    sentence_to_list = sentence.split()
    length_of_list = len(sentence_to_list)
    
    new_list = [None for i in range(length_of_list)]
    
    for word in sentence_to_list:
        for i in word:
            if i in numbers:
                new_list[int(i)-1] = word

    return ' '.join(new_list)
