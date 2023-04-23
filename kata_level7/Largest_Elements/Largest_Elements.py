def largest(n, xs):
    a = sorted(xs)
    return a[len(a)-n:]
