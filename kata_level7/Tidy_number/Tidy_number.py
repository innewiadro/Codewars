def tidyNumber(n):
    int_list = [int(i) for i in str(n)]

    for j in range(len(int_list) - 1):
        if int_list[j] > int_list[j + 1]:
            return False
    return True
