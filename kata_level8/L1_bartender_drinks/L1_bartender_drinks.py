def get_drink_by_profession(param):
    profession_to_drink = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal"
    }

    lowercased_profession = param.lower()

    return profession_to_drink.get(lowercased_profession, "Beer")
