def top3(products, amounts, prices):
    revenues = [(amounts[i] * prices[i], -i, products[i]) for i in range(len(products))]
    revenues.sort(reverse=True)
    return [product for _, _, product in revenues[:3]]
