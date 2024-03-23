def solve(strings: list[str]) -> list[int]:
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    counter = 0
    number = 0
    res = []
    for i in strings:
        for j in i.lower():
            if j == alpha[number]:
                counter += 1
            number += 1

            if number > 25:
                break

        res.append(counter)
        counter = 0
        number = 0
    return res
