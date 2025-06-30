def generate_number(squad, n):
    if n not in squad:
        return n

    for i in range(1, 10):
        for j in range(1, 10):
            if i + j == n:
                candidate = int(f"{i}{j}")
                if candidate not in squad:
                    return candidate
    return None

