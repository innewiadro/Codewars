def solution(stones):
    removals = 0
    for i in range(1, len(stones)):
        if stones[i] == stones[i - 1]:
            removals += 1
    return removals
