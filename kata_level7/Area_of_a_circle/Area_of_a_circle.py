def circle_area(r):
    if r <= 0:
        raise ValueError("Radius must be positive.")
    else:
        return r**2 * 3.141
