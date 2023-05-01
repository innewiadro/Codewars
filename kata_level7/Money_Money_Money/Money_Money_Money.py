def calculate_years(principal, interest, tax, desired):
    count = 0
    sum = principal
    while sum < desired:
        
        profit = sum * interest - (sum * interest * tax)
        sum += profit
        count += 1
        
    return count 
