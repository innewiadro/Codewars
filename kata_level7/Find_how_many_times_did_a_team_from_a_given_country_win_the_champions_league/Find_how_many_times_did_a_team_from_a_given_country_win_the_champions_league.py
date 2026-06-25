def count_wins(winners_list, country):
    return len([winner for winner in winners_list if winner["country"] == country])