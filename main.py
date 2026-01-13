from task_manager import TaskManager

manager = TaskManager()

while True:
    task = input("Enter a task (or type 'exit' to quit): ")
    if task == "exit":
        break
    manager.add_task(task)

print("\nYour tasks:")
for task in manager.get_tasks():
    print("-", task)
