def pillars(num_pill, dist, width):
    return (num_pill-2) * width + (num_pill - 1) * dist * 100 if num_pill > 1 else 0
