def peak_and_valley(arr):
    result = []

    for i in range(3, len(arr) - 3):
        left = arr[i - 3:i]
        right = arr[i + 1:i + 4]

        if not left or not right:
            continue

        if arr[i] > max(left) and arr[i] > max(right):
            result.append(arr[i])
        elif arr[i] < min(left) and arr[i] < min(right):
            result.append(arr[i])

    return result