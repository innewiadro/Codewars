def sentence(lst):
    sorted_data = sorted(lst, key=lambda d: int(list(d.keys())[0]))
    values = [list(i.values())[0] for i in sorted_data]
    return " ".join(values)
