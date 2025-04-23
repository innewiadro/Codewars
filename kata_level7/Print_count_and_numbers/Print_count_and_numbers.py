def count_me(data):
    if not data or not data.isdigit():
        return ""

    result = []
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
        result.append(f"{count}{data[i]}")
        i += 1
    return ''.join(result)
