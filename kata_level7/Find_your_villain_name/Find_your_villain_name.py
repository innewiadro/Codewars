def get_villain_name(birthdate):
    first = ["The Evil", "The Vile", "The Cruel", "The Trashy", "The Despicable", "The Embarrassing",
             "The Disreputable", "The Atrocious", "The Twirling", "The Orange", "The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat",
            "Teaspoon", "Laundry Basket"]

    first_name = first[birthdate.month - 1]
    last_name = last[birthdate.day % 10]

    return f"{first_name} {last_name}"
