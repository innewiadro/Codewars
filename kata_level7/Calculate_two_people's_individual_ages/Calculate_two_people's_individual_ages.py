def get_ages(sum_, difference):
    a = sum_/2 + difference/2
    b = sum_/2 - difference/2
    return (a, b) if (sum_ >= 0 and difference >= 0 and sum_ >= difference) else None
