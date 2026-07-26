class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True


class ImportantTask(Task):
    def __init__(self, title):
        super().__init__(title)
        self.priority = "High"