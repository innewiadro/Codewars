def yoga(classroom, poses):
    total_completed = 0

    for row in classroom:
        row_sum = sum(row)
        for pose in poses:
            for person_skill in row:
                if row_sum + person_skill >= pose:
                    total_completed += 1

    return total_completed
