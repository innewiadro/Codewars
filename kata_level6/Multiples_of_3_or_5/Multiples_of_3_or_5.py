def solution(number):
    new_set = set()
    for i in range(number):
        if i % 3 == 0:
            new_set.add(i)

        if i % 5 == 0:
            new_set.add(i)

    return sum(new_set)

