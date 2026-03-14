import pytest
from unittest.mock import mock_open, patch
from src.recieve_tasks import receive
from src.classes.task_source_protocol import TaskSource
from src.classes.task_dataclass import Task
from src.TaskSources.file_task import FileTaskSource
from src.TaskSources.task_generator import TaskGenerator
from src.TaskSources.api_task import ApiTaskSource
from src.exceptions.file_task_source_exceptions import FileTaskSourceNotFound

class NotSource:
    pass

def test_receive_with_file_source():
    mock_file_content = "1 test\n"
    m_open = mock_open(read_data=mock_file_content)
    with patch("builtins.open", m_open):
        source = FileTaskSource("file.txt")
        tasks = receive(source)
    assert len(tasks) == 1
    assert tasks[0].id == "1"

def test_receive_with_generator():
    source = TaskGenerator(2)
    tasks = receive(source)
    assert len(tasks) == 2

def test_receive_with_api_source():
    source = ApiTaskSource(2)
    tasks = receive(source)
    assert len(tasks) == 2

def test_receive_raises_on_non_protocol():
    source = NotSource()
    with pytest.raises(TypeError, match="не реализует протокол TaskSource"):
        receive(source)

def test_receive_passes_through_exceptions():
    source = FileTaskSource("missing.txt")
    with pytest.raises(FileTaskSourceNotFound):
        receive(source)