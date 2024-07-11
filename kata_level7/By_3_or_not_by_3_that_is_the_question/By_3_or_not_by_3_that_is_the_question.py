def divisible_by_three(st):
    while len(st) >= 1:
        st = str(sum([int(i) for i in list(st)]))

        if st == "3" or st == "6" or st == "9":
            return True
        if len(st) < 2:
            return False
