def max_rot(n):

    num_str = str(n)
    max_num = n

    for i in range(len(num_str) - 1):

        num_str = num_str[:i] + num_str[i + 1:] + num_str[i]

        rotated_num = int(num_str)

        if rotated_num > max_num:
            max_num = rotated_num

    return max_num
