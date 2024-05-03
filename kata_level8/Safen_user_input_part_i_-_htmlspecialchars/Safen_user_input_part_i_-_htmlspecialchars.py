def html_special_chars(data):
    swap = {"<": "&lt;", ">": "&gt;", "\"": "&quot;", "&": "&amp;"}
    return "".join([swap.get(i, i) for i in data])
