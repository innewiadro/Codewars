def filter_long_words(sentence, n):
    res=[]
    for i in sentence.split():
        if len(i) > n:
            res.append(i)
    return res
