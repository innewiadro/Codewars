def rake_garden(garden):
    items = garden.split()
    raked_items = ['gravel' if item not in {'rock', 'gravel'} else item for item in items]
    return ' '.join(raked_items)
