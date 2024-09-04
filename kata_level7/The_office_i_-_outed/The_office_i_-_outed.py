def outed(meet, boss):
    total_score = 0
    number_of_people = len(meet)

    for person, score in meet.items():
        if person == boss:
            total_score += score * 2
        else:
            total_score += score

    average_score = total_score / number_of_people

    if average_score <= 5:
        return "Get Out Now!"
    else:
        return "Nice Work Champ!"