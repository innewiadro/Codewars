def sum_no_duplicates(number_list):
    new_set = set()
    for i in number_list:
        new_set.add(i)
        if number_list.count(i) > 1:
            new_set.remove(i)

    return sum(new_set)
