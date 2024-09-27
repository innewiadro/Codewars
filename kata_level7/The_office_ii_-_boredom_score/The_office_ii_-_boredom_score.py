def boredom(staff):
    depart = {
        'accounts': 1,
        'finance': 2,
        'canteen': 10,
        'regulation': 3,
        'trading': 6,
        'change': 6,
        'IS': 8,
        'retail': 5,
        'cleaning': 4,
        'pissing about': 25
    }

    total_score = sum(depart.get(dept, 0) for dept in staff.values())

    if total_score <= 80:
        return 'kill me now'
    elif 80 < total_score < 100:
        return 'i can handle this'
    else:
        return 'party time!!'
