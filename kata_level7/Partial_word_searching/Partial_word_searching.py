def word_search(query, seq):
    res = []
    for i in seq:
        if query.lower() in i.lower():
            res.append(i)
    return res if len(res) > 0 else ['None']
