def total_amount_visible(top_num, num_of_sides):
    totalDots = num_of_sides * (num_of_sides + 1) // 2
    bottomNum = (num_of_sides + 1) - top_num
    return totalDots - bottomNum
