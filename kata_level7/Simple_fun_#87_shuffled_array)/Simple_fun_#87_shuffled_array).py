def shuffled_array(s):
    total = sum(s)

    for x in s:
        if total - x == x:
            result = s.copy()
            result.remove(x)
            return sorted(result)