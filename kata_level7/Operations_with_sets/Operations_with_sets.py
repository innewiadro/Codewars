def process_2arrays(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    common = set1 & set2
    only_one = set1 ^ set2
    remaining_arr1 = set1 - set2
    remaining_arr2 = set2 - set1

    return [len(common), len(only_one), len(remaining_arr1), len(remaining_arr2)]
