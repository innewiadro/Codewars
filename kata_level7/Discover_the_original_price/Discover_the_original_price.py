from decimal import Decimal, ROUND_HALF_UP


def discover_original_price(discounted_price, sale_percentage):
    sale_price = Decimal(discounted_price)

    original_price = sale_price / (Decimal(1) - (Decimal(sale_percentage) / Decimal(100)))

    original_price = original_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    return float(original_price)
