def who_is_serving(currentRound: int) -> int:
    if currentRound <= 0:
        raise ValueError("Round must be a positive integer")

    return 1 if ((currentRound - 1) // 2) % 2 == 0 else 2
