def remove_rotten(bag_of_fruits):
    new_bag = []
    if bag_of_fruits is not None:
        for i in bag_of_fruits:
            if "rotten" in i:
                new_bag.append(i[6:].lower())
            else:
                new_bag.append(i)

    return new_bag
