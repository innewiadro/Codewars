def is_planet_mnemonic_correct(solar_system, mnemonic):
    filtered_planets = [planet for planet in solar_system if planet != "Asteroid"]

    words = mnemonic.split()

    if len(words) != len(filtered_planets):
        return False

    return all(word[0].upper() == planet[0].upper() for word, planet in zip(words, filtered_planets))
