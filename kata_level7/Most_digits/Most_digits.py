def find_longest(arr):
    string = ""
    for i in arr:
        if len(str(i)) > len(string):
            string = str(i)
    return int(string)
