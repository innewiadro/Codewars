def histogram(results):
    output = ""
    for i in range(6, 0, -1):
        count = results[i - 1]
        if count > 0:
            output += f"{i}|{'#' * count} {count}\n"
        else:
            output += f"{i}|\n"
    return output
