def calculate_priority(task):
    days = task.days_remaining()
    if days <= 0:
        urgency = 6
    elif days <= 3:
        urgency = 5
    elif days <= 7:
        urgency = 3
    else:
        urgency = 1
    return (task.difficulty * 2) + urgency
def allocate_study_time(tasks, daily_limit):
    active_tasks = [t for t in tasks if t.remaining_hours > 0]
    total_priority = sum(calculate_priority(t) for t in active_tasks)
    schedule = []
    for task in active_tasks:
        weight = calculate_priority(task) / total_priority
        allocated = round(weight * daily_limit, 1)
        allocated = min(allocated, task.remaining_hours)
        if allocated > 0:
            schedule.append((task, allocated))
    return schedule
