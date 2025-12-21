from datetime import date

class Task:
    def __init__(self, subject, name, deadline, difficulty, total_hours):
        self.subject = subject
        self.name = name
        self.deadline = deadline
        self.difficulty = difficulty
        self.remaining_hours = total_hours

    def days_remaining(self):
        return (self.deadline - date.today()).days

    def is_complete(self):
        return self.remaining_hours <= 0
    def is_overdue(self):
        return self.days_remaining() < 0
