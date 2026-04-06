from preloaded import Like, Dislike, Nothing

def like_or_dislike(lst):
    state = "Nothing"

    for i in lst:
        if state == i:
            state = "Nothing"
        else:
            state = i

    return state