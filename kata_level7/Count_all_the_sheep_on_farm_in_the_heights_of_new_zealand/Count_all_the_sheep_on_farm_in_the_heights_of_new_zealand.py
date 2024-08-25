def lost_sheep(friday_counts, saturday_counts, total_sheep):
    total_returned = sum(friday_counts) + sum(saturday_counts)
    lost_sheep_res = total_sheep - total_returned
    return lost_sheep_res
