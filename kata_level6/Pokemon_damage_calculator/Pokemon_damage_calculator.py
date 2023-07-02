def calculate_damage(your_type, opponent_type, attack, defense):
    type_pokemon = {'fire': {"grass": 2,
                             "water": 0.5,
                             "electric": 1,
                             "fire": 0.5},
                    'grass': {"fire": 0.5,
                              "water": 2,
                              "electric": 1,
                              "grass": 0.5},
                    'water': {"grass": 0.5,
                              "fire": 2,
                              "electric": 0.5,
                              "water": 0.5},
                    'electric': {"grass": 1,
                                 "water": 2,
                                 "fire": 1,
                                 "electric": 0.5}}
    
    damage = 50 * (attack / defense) * type_pokemon[your_type][opponent_type]
    return damage
