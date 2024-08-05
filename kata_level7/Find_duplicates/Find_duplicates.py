def duplicates(arr):
    seen = set()
    duplicates = set()
    result = []

    for item in arr:
        if item in seen:
            if item not in duplicates:
                duplicates.add(item)
                result.append(item)
        else:
            seen.add(item)

    return result
