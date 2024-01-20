def get_order(order):
    order_string = ""
    menu_list = {'burger': 'Burger',
                 'fries': 'Fries',
                 'chicken': 'Chicken',
                 'pizza': 'Pizza',
                 'sandwich': 'Sandwich',
                 'onionrings': 'Onionrings',
                 'milkshake': 'Milkshake',
                 'coke': 'Coke'}

    for i in menu_list:
        number = order.count(i)
        order_string += (menu_list[i] + " ") * number

    return order_string[:-1]
