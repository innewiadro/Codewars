def dropzone(fire, dropzones):
    fx, fy = fire

    def distance(dz):
        return (dz[0] - fx) ** 2 + (dz[1] - fy) ** 2

    return min(dropzones, key=distance)
