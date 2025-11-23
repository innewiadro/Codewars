def pattern(n: int) -> str:
    return "" if n <= 0 else "\n".join("".join(str((i + j - 1) % n + 1) for j in range(n)) for i in range(1, n + 1))