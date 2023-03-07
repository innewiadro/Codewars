def queue_time(customers, n):
    list_of_q = [0 for i in range(n)]
    minimum_index = 0
    list_length = len(list_of_q)

    for i in customers:
        for index in range(list_length):
            if list_of_q[index] < list_of_q[minimum_index]:
                minimum_index = index
        list_of_q[minimum_index] += i

    return max(list_of_q)
