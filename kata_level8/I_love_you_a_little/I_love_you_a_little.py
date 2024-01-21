def how_much_i_love_you(nb_petals):
    love_list = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    return love_list[(nb_petals - 1) % 6]
