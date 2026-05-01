def sum_average(lists: list[list[int]]) -> float:
    return sum(sum(list) / len(list) for list in lists)