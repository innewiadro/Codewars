def flatten(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(item)
    else:
        flattened.append(item)

    return flattened