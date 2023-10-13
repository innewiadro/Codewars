def cookie(x):
    if type(x) is str:
        text = "Zach"
    elif type(x) is bool:
        text = "the dog"
    else:
        text = "Monica"
    return f"Who ate the last cookie? It was {text}!"
