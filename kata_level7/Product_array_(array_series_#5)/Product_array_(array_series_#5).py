def product_array(numbers):
    prod = 1
    for element in numbers:
        prod *= element

    return [prod / i for i in numbers]
