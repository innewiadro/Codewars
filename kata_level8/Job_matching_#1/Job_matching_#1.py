def job_matching(candidate, job):
    if 'min_salary' not in candidate or 'max_salary' not in job:
        raise ValueError("Candidate must have 'min_salary' and job must have 'max_salary'")

    min_salary_with_wiggle = candidate['min_salary'] * 0.9
    return min_salary_with_wiggle <= job['max_salary']
