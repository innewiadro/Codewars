def travel(total_time, run_time, rest_time, speed):
    if total_time <= 0 or run_time <= 0 or speed <= 0:
        return 0

    cycle_time = run_time + rest_time
    full_cycles = total_time // cycle_time
    remaining_time = total_time % cycle_time

    distance_in_full_cycles = full_cycles * run_time * speed
    distance_in_remaining_time = min(remaining_time, run_time) * speed

    return distance_in_full_cycles + distance_in_remaining_time
