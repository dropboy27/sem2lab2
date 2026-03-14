from src.classes.task_dataclass import Task

def test_task_creation():
    task = Task(id="123", payload="test")
    assert task.id == "123"
    assert task.payload == "test"