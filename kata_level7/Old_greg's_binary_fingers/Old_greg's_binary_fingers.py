def binary_fingers(bin_string):
    fingers = ["Pinkie", "Ring", "Middle", "Index", "Thumb"]
    padded = bin_string.zfill(5)
    return [fingers[i] for i in range(5) if padded[i] == '1']
