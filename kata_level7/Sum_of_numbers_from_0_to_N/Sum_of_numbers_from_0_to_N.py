def show_sequence(n):
    if n < 0:
        return f"{n}<0"
    elif n == 0:
        return "0=0"
    else:
        return "+".join([str(i) for i in range(n+1)]) + " = " + str(sum([i for i in range(n+1)]))
