def wave(people):
    list_of_word=[]
    for i in range(len(people)):
        if people[i] != " ":
            print(i)
            result = people[0:i] + people[i].upper() + people[i+1:]
            list_of_word.append(result)
       
    return list_of_word
