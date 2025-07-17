def find_nth_occurrence(substring, string, occurrence=1):
    count = 0
    index = 0

    while index <= len(string) - len(substring):
        if string[index:index + len(substring)] == substring:
            count += 1
            if count == occurrence:
                return index
        index += 1

    return -1