import math

def movie(card, ticket, perc):
    n = 0
    cost_system_a = 0
    cost_system_b = card
    current_ticket_price = ticket

    while math.ceil(cost_system_b) >= cost_system_a:
        n += 1
        cost_system_a = ticket * n
        current_ticket_price *= perc
        cost_system_b += current_ticket_price

    return n
