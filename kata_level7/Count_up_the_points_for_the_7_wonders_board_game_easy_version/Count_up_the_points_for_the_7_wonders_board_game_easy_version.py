def seven_wonders_science(compasses, gears, tablets):
    complete_sets = min(compasses, gears, tablets)
    step1_points = complete_sets * 7

    step2_points = compasses**2 + gears**2 + tablets**2

    total_score = step1_points + step2_points
    return total_score
