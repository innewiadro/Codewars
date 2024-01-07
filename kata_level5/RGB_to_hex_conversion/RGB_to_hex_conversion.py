def rgb(r, g, b):
    rgb_list = [r, g, b]
    new_rgb = []
    conv = ""
    counter = 0

    for i in rgb_list:
        if i < 0:
            a = 0
        elif i > 255:
            a = 255
        else:
            a = i

        new_rgb.append(a)

    for j in new_rgb:
        if len(hex(new_rgb[counter])[2:]) < 2:
            conv += "0" + hex(new_rgb[counter])[2:]
        else:
            conv += hex(new_rgb[counter])[2:]

        counter += 1

    return conv.upper()
