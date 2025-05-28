def replace_nth(text, n, old_value, new_value):
    if n <= 0 or text.count(old_value) < n:
        return text

    count = 0
    result = []

    for ch in text:
        if ch == old_value:
            count += 1
            if count % n == 0:
                result.append(new_value)
            else:
                result.append(ch)
        else:
            result.append(ch)

    return ''.join(result)