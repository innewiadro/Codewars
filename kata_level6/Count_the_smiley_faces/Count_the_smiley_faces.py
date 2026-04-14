import re


def count_smileys(arr):
    return sum(1 for face in arr if re.match(r'^[:;][-~]?[)D]$', face))
