import pytest
from unittest.mock import patch
from src.main import main
from src.classes.task_dataclass import Task

def test_main_exit(capsys):
    """Выход по пункту 5."""
    with patch('builtins.input', return_value='5'):
        main()
    captured = capsys.readouterr()
    assert "exit" in captured.out.lower() or "выход" in captured.out.lower()


def test_main_invalid_choice(capsys):
    """Ввод неверного пункта меню (должно быть сообщение об ошибке)."""
    inputs = ['99', '5']
    with patch('builtins.input', side_effect=inputs):
        main()
    captured = capsys.readouterr()
    assert 'неверный пункт меню' in captured.out.lower()