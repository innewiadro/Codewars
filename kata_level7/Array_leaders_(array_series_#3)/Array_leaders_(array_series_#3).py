def array_leaders(arr):
    n = len(arr)
    leaders = []
    total_sum = 0

    for i in range(n - 1, -1, -1):
        if arr[i] > total_sum:
            leaders.append(arr[i])
        total_sum += arr[i]
    leaders.reverse()

    return leaders
