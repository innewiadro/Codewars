def type_of_function(domain, codomain, relations):

    mapping = {}

    for x, y in relations:
        if x in mapping:
            return "It is not a function"
        mapping[x] = y

    if set(mapping.keys()) != set(domain):
        return "It is not a function"

    values = list(mapping.values())

    is_injective = len(values) == len(set(values))

    is_surjective = set(values) == set(codomain)

    if is_injective and is_surjective:
        return "Bijective"
    elif is_injective:
        return "Injective"
    elif is_surjective:
        return "Surjective"
    else:
        return "General function"

