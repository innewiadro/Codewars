def how_many_times(annual_price, individual_price):
    return (annual_price // individual_price) + (1 if annual_price % individual_price != 0 else 0)
