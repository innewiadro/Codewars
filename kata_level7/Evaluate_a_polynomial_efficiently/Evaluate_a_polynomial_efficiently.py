def evaluate_polynomial(coefficients: list[int], x: int) -> int:
    result = 0
    for coef in coefficients:
        result = result * x + coef
    return result