def solve(arr):
    arr = arr[::-1]
    return [f"Begin on {arr[0].split(' on ')[1]}"] + [
        f"{'Left' if arr[i-1].startswith('Right') else 'Right'} on {arr[i].split(' on ')[1]}"
        for i in range(1, len(arr))
    ]
