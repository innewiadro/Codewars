def switcheroo(s):
    swap = {"a": "b", "b": "a", "c": "c"}
    return "".join([swap[i] for i in s])
