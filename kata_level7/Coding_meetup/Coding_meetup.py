def count_developers(lst):
    return len([
        dev for dev in lst
        if dev['continent'] == 'Europe' and dev['language'] == 'JavaScript'
    ])