def head(xs):
    if not xs:
        raise ValueError("head of empty list")
    return xs[0]

def tail(xs):
    if not xs:
        raise ValueError("tail of empty list")
    return xs[1:]

def init(xs):
    if not xs:
        raise ValueError("init of empty list")
    return xs[:-1]

def last(xs):
    if not xs:
        raise ValueError("last of empty list")
    return xs[-1]
