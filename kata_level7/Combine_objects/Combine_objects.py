
def combine(*objects):
    combined = {}
    for obj in objects:
        for key, value in obj.items():
            combined[key] = combined.get(key, 0) + value
    return combined
