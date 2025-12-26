from task import Task
from schedules import calculate_priority, allocate_study_time
from utils import parse_date

tasks = []
print(" Smart Study Planner\n")
num_tasks = int(input("How many tasks do you have? "))
for i in range(num_tasks):
    print(f"\nTask {i + 1}")
    subject = input(f"Subject {i + 1}: ")
    name = input("Task name: ")
    deadline = parse_date(input("Deadline (YYYY-MM-DD): "))
    difficulty = int(input("Difficulty (1–5): "))
    hours = int(input("Total hours needed: "))
    tasks.append(Task(subject, name, deadline, difficulty, hours))

daily_limit = int(input("\nHow many hours can you study now? "))
print("\n Study Session Plan\n")
tasks.sort(key=calculate_priority, reverse=True)
study_plan = allocate_study_time(tasks, daily_limit)
for task, hours in study_plan:
    task.remaining_hours -= hours
    print(
        f"- {task.subject}: {task.name} → {hours} hrs "
        f"(remaining total: {task.remaining_hours} hrs)"
    )
