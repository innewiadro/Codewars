def print_array(arr):
    string = ""
    if len(arr) > 1:
        for i in arr:
            string += str(i) + ","
        return string[:len(string)-1]
    else:
        return str(arr[0])
