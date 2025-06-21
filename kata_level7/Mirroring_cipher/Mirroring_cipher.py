def mirror(text, mirror_set=None):
    text = text.lower()

    if mirror_set is None:
        mirror_set = 'abcdefghijklmnopqrstuvwxyz'

    mirror_set = mirror_set.lower()

    mirror_map = {}
    for i in range(len(mirror_set)):
        mirror_map[mirror_set[i]] = mirror_set[-i - 1]

    result = ''
    for char in text:
        result += mirror_map.get(char, char)

    return result
