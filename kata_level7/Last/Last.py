def last(*args):
    if len(args) == 1 and isinstance(args[0], (list, str)):
        return args[0][-1]

    return args[-1]
