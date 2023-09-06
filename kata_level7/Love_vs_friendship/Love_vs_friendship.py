def words_to_marks(s):
    abc = list(map(chr, range(97, 123)))
    data = {val: key for key, val in enumerate(abc, 1) }
    return sum(data[x] for x in s)
