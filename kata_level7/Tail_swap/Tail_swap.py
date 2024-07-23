def tail_swap(strings):
    first_part1, second_part1 = strings[0].split(":")
    first_part2, second_part2 = strings[1].split(":")

    new_string1 = first_part1 + ":" + second_part2
    new_string2 = first_part2 + ":" + second_part1

    return [new_string1, new_string2]
