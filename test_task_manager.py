from task_manager import TaskManager

def test_add_task():
    manager = TaskManager()
    manager.add_task("Test task")
    assert len(manager.get_tasks()) == 1

def test_get_tasks():
    manager = TaskManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    assert manager.get_tasks() == ["Task 1", "Task 2"]
  
