def add_length(str_):
    results = []
    for i in str_.split(" "):
        results.append(i + " " + str(len(i)))
    return results
