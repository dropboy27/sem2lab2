from src.classes.task_dataclass import Task
from src.exceptions.file_task_source_exceptions import FileTaskSourceNotFound

class FileTaskSource:
    """Источник задач из текстового файла."""
    def __init__(self, filename: str):
        """Инициализация с именем файла."""
        self.filename = filename

    def get_tasks(self) -> list[Task]:
        """Читает задачи из файла и возвращает список Task."""
        tasks = []
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    parts = line.split()
                    if len(parts) >= 2:
                        tasks.append(Task(id=parts[0], payload=parts[1]))
        except FileNotFoundError as e:
            raise FileTaskSourceNotFound(self.filename) from e
        return tasks