from functools import reduce


def share_price(invested, changes):
    final_price = reduce(lambda acc, pct: acc * (1 + pct / 100), changes, invested)
    return f"{final_price:.2f}"
