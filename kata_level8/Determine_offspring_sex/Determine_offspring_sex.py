def chromosome_check(chromosome):
    gender = {'XY': "son",
              'XX': "daughter"}
    txt = f'Congratulations! You\'re going to have a {gender[chromosome]}.'
    return txt
