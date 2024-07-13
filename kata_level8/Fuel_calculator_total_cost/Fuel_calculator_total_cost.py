def fuel_price(litres, price_per_litre):
    discount_per_litre = min((litres // 2) * 0.05, 0.25)
    discounted_price_per_litre = price_per_litre - discount_per_litre
    total_cost = litres * discounted_price_per_litre
    return total_cost
