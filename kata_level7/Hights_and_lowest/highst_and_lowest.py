def high_and_low(numbers):
    string_to_list = [int(s) for s in numbers.split(" ")]
    return print("%d %d" % (max(string_to_list), min(string_to_list)))

