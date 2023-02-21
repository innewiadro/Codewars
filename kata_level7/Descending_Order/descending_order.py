def descending_order(num):
    if num > 0:
        new_num = list(str(num))
        new_num.sort(reverse=True)
        a = "".join(new_num)
        return int(a)
