def cakes(recipe, available):
    recipe_list = []
    try:
        for k, v in recipe.items():
            recipe_list.append(available[k] // recipe[k])
            
        return min(recipe_list)
    except:
        return 0
