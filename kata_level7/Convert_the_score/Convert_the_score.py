def scoreboard(st):
    res = st.split()
    last = []
    score = ["nil","one","two", "three", "four", "five","six", "seven", "eight", "nine"]
    for i in res:
        if i in score:
            last.append(score.index(i))

    return last
