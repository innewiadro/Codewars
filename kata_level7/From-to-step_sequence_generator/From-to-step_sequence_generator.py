def generator (_from, _to, _step):
    if _step <= 0:
        return []

    result = []
    if _from <= _to:
        current = _from
        while current <= _to:
            result.append(current)
            current += _step
    else:
        current = _from
        while current >= _to:
            result.append(current)
            current -= _step
    return result
