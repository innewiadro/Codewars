def fizzbuzz(n):
    summary = []
    for i in range(1, n + 1):
        res = ""
        if i % 3 == 0:
            res += "Fizz"
        if i % 5 == 0:
            res += "Buzz"

        if len(res) == 0:
            summary.append(i)
        else:
            summary.append(res)

    return summary
