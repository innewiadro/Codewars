def meeting(s):
    string_to_list = []
    for i in s.upper().split(';'):
        string_to_list.append(i.split(':'))
               
    sorted_name_list = sorted(string_to_list, key=(lambda name: (name[1], name[0])))

    summary = ''
    string = ''
    for i in sorted_name_list:
        count = 1
        for j in i[::-1]:      
            if count % 2 != 0:
                string += '(' + j + ", " 
                count += 1
            else:
                string += j + ')'
                count += 1
            
    summary += string
    return summary
