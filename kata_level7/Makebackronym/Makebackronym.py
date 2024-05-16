def make_backronym(acronym):
    return " ".join([dictionary[i.upper()] for i in acronym])
