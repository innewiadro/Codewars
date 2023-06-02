from collections import Counter


def score(dice):
    total = 0
    points = {1: 1000,
              2: 200,
              3: 300,
              4: 400,
              5: 500,
              6: 600}
    throw = Counter(dice)
    
    for k, v in throw.items():
        if v >= 3:
            total += points[k]
        if k == 1:
            total += 100 * (v % 3)
        if k == 5:
            total += 50 * (v % 3)
            
    return total
