def michael_pays(cost):
    if cost < 5:
        return round(cost, 2)
    else:
        kate_share = min(cost / 3, 10)
        michael_share = cost - kate_share
        return round(michael_share, 2)
