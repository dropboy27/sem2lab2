from src.classes.task_source_protocol import TaskSource
from src.classes.task_dataclass import Task

class GoodSource:
    def get_tasks(self) -> list[Task]:
        return [Task("1", "test")]

class BadSource:
    pass

def test_protocol_runtime_checkable():
    assert isinstance(GoodSource(), TaskSource)
    assert not isinstance(BadSource(), TaskSource)