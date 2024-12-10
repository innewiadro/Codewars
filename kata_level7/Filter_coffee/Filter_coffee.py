def search(budget, prices):
    affordable_prices = [price for price in prices if price <= budget]
    affordable_prices.sort()

    return ",".join(map(str, affordable_prices))
