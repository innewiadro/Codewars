def head_smash(arr):
    if isinstance(arr, int):
        return "This isn't the gym!!"

    if arr == [] or arr == "":
        return "Gym is empty"

    return [row.replace('O', ' ') for row in arr]
