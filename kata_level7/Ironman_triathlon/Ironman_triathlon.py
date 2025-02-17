def i_tri(s):
    total_race = 2.4 + 112 + 26.2  # Total race distance in miles
    remaining = total_race - s

    if remaining == total_race:
        return "Starting Line... Good Luck!"
    elif remaining <= 0:
        return "You're done! Stop running!"

    formatted_distance = f"{remaining:.2f} to go!"  # Ensuring two decimal places

    if remaining > (112 + 26.2):
        return {"Swim": formatted_distance}
    elif remaining > 26.2:
        return {"Bike": formatted_distance}
    elif remaining > 10:
        return {"Run": formatted_distance}
    else:
        return {"Run": "Nearly there!"}
