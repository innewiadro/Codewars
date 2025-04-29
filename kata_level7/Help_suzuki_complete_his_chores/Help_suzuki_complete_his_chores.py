def chore_assignment(chores):
    chores.sort()
    n = len(chores) // 2
    workloads = [chores[i] + chores[-i-1] for i in range(n)]
    return sorted(workloads)
