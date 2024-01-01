def balanced_num(number):
    if len(str(number)) < 3:
        return "Balanced"

    else:
        if len(str(number)) % 2 != 0:
            left = list(str(number)[0:len(str(number)) // 2])
            right = list(str(number)[(len(str(number)) // 2) + 1:])

            return "Balanced" if sum([int(i) for i in left]) == sum([int(i) for i in right]) else "Not Balanced"

        else:
            left = list(str(number)[0:len(str(number)) // 2 - 1])
            right = list(str(number)[(len(str(number)) // 2) + 1:])

            return "Balanced" if sum([int(i) for i in left]) == sum([int(i) for i in right]) else "Not Balanced"
