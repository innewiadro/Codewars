def mirror(data: list) -> list:
    if not data:
        return []

    sorted_data = sorted(data)

    mirrored = sorted_data + sorted_data[-2::-1]
    return mirrored
