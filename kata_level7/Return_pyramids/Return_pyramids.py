def pyramid(n):
    lines = []

    for i in range(1, n + 1):
        spaces = n - i

        if i == n:
            middle = "_" * (2 * (n - 1))
        else:
            middle = " " * (2 * (i - 1))

        line = " " * spaces + "/" + middle + "\\"
        lines.append(line)

    return "\n".join(lines) + "\n"