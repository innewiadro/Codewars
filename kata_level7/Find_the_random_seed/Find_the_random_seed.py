import random


def find_seed(target_sequence):
    for seed in range(10000):
        random.seed(seed)
        generated = [random.randint(0, 100) for _ in range(10)]
        if generated == target_sequence:
            return seed
    return None
