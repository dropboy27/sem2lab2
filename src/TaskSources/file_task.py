from src.classes.task_dataclass import Task
from src.exceptions.file_task_source_exceptions import FileTaskSourceNotFound
from src.exceptions.task_exceptions import TaskError

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
                    if len(parts) >= 4:
                        try:
                            task = Task(
                                id=int(parts[0]),
                                description=parts[1],
                                priority=int(parts[2]),
                                status=parts[3]
                            )
                            tasks.append(task)
                        except (TaskError) as e:
                            print(f"Ошибка в строке '{line.strip()}': {e}")
        except FileTaskSourceNotFound as e:
            raise FileTaskSourceNotFound(self.filename) from e
        return tasks