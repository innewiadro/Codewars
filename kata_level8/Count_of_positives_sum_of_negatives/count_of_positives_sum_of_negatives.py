def count_positives_sum_negatives(arr):
    if len(arr) > 0:
        return [len([p for p in arr if p > 0]), sum([n for n in arr if n < 0])]
    else:
        return []
