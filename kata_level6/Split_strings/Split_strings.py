def solution(s):
    results = []
    list_of_letter = list(s)
    if len(list_of_letter) % 2 != 0:
        list_of_letter.append("_")
    for i in range(0,len(list_of_letter),2):
        results.append(''.join(list_of_letter[i:i+2]))
        
    return results

if __name__ == '__main__':
    print(solution('abcdefg'))
