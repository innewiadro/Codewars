def archers_ready(archers):
    return all(element > 4 for element in archers) if len(archers) > 0 else False
