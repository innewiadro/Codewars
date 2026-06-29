def uncensor(infected, discovered):
    result = []
    i = 0

    for char in infected:
        if char == "*":
            result.append(discovered[i])
            i += 1
        else:
            result.append(char)

    return "".join(result)