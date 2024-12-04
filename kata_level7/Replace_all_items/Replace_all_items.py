def replace_all(obj, find, replace):
    if isinstance(obj, list):
        return [replace if x == find else x for x in obj]
    elif isinstance(obj, str):
        return obj.replace(find, replace)
    else:
        raise TypeError("Input must be a string or a list")
