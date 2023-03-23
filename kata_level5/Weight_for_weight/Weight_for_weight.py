def count_weight(strng):
    return sum(int(x) for x in strng), strng
    

def order_weight(strng):
    return ' '.join(sorted(strng.split(' '), key=count_weight))
