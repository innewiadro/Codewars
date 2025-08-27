def has_loop(arr: list[int]) -> bool:
    visited = set()
    index = 0

    while 0 <= index < len(arr):
        if index in visited:
            return True
        visited.add(index)
        index = arr[index]

    return False
