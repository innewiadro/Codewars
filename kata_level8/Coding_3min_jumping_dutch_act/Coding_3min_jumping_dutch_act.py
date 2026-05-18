def sc(n: int) -> str:
    if n <= 1:
        return ""

    result = "Aa~ " * (n - 1) + "Pa!"

    if n <= 6:
        result += " Aa!"

    return result
