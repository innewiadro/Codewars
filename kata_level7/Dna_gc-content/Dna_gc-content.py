import math


def gc_content(seq):
    if not seq:
        return 0.0

    gc_count = sum(1 for base in seq.upper() if base in 'GC')
    gc_percentage = (gc_count / len(seq)) * 100

    return math.ceil(gc_percentage * 100) / 100
