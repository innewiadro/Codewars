def add(a):
    def inner(x):
        return a + x
    return inner
