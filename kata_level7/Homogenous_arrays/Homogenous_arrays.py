def filter_homogenous(arrays):
    return [sub for sub in arrays if sub and all(isinstance(x, type(sub[0])) for x in sub)]
