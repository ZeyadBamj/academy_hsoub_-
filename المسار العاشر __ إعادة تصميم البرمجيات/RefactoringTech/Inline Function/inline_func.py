class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True
        print(self.name, "Completed")
        # self.print_completed_message()

    # def print_completed_message(self):
    #     if self.completed:
    #         print(self.name, "Completed")

    def __str__(self):
        return "{name}: {description}, status: {completed}".format(name=self.name, description=self.description, completed=self.completed)

if __name__ == "__main__":
    task1 = Task(name="Shopping", description="Buy some groceries")
    print(task1)
    task1.complete()