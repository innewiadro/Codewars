def bouncing_ball(h, bounce, window):
    if 0 < bounce < 1 and window < h and h > 0:
        number_of_views = 1
        while h * bounce > window:
            h = h * bounce
            number_of_views += 1
            if h > window:
                number_of_views += 1

        return number_of_views

    else:
        return -1
