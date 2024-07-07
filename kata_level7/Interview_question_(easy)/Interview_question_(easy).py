def get_strings(city):
    city = city.lower().replace(" ", "")
    city = list(city)
    new_d = dict()
    res = ""
    for i in city:
        if i not in new_d:
            new_d[i] = "*"
        else:
            a = len(new_d[i]) + 1
            new_d[i] = a * "*"

    for k, v in new_d.items():
        res += f'{k}:{v},'
    return res[:-1]
