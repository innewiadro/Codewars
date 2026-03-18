def merge_strings(first, second):
    max_overlap = min(len(first), len(second))

    for i in range(max_overlap, 0, -1):
        if first[-i:] == second[:i]:
            return first + second[i:]

    return first + second