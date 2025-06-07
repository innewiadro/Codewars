def is_cleanly_nested(arr):
    if not isinstance(arr, list):
        return False

    if not arr:
        return True

    if not all(isinstance(child, list) for child in arr):
        return False

    dead_ends = [child for child in arr if child == []]
    nested = [child for child in arr if child != []]


    if dead_ends and nested:
        return False

    return all(is_cleanly_nested(child) for child in arr)