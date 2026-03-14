import pytest
from unittest.mock import mock_open, patch
from src.TaskSources.file_task import FileTaskSource
from src.exceptions.file_task_source_exceptions import FileTaskSourceNotFound
from src.classes.task_dataclass import Task

def test_file_task_source_reads_lines():
    mock_file_content = "1 task1\n2 task2\n3 task3 with extra\n"
    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        source = FileTaskSource("file.txt")
        tasks = source.get_tasks()
        assert len(tasks) == 3
        assert tasks[0] == Task(id="1", payload="task1")
        assert tasks[1] == Task(id="2", payload="task2")
        assert tasks[2] == Task(id="3", payload="task3") 

def test_file_task_source_empty_file():
    with patch("builtins.open", mock_open(read_data="")):
        source = FileTaskSource("empty.txt")
        tasks = source.get_tasks()
        assert tasks == []

def test_file_task_source_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        source = FileTaskSource("missing.txt")
        with pytest.raises(FileTaskSourceNotFound) as excinfo:
            source.get_tasks()
        assert "missing.txt" in str(excinfo.value)

def test_file_task_source_ignores_malformed_lines():
    mock_content = "1 task1\nbadline\n3 task3\n"
    with patch("builtins.open", mock_open(read_data=mock_content)):
        source = FileTaskSource("file.txt")
        tasks = source.get_tasks()
        assert len(tasks) == 2
        assert tasks[0].id == "1"
        assert tasks[1].id == "3"