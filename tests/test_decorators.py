import pytest
from src.decorators import log


def test_error_console(capsys):
    @log()
    def my_function(x, y):
        return x + y
    with pytest.raises(TypeError):
        my_function(2, "3")
    captured = capsys.readouterr()
    assert "my_function error: <class 'TypeError'>. args: (2, '3'), kwargs: {}\n\n" == captured.out


def test_success_console(capsys):
    @log()
    def my_function(x, y):
        return x + y
    result = my_function(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    assert "my_function ok 5\n\n" == captured.out


def test_success_file():
    file_name = "test.txt"

    @log(filename=file_name)
    def my_function(x, y):
        return x + y
    result = my_function(2, 3)
    assert result == 5
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.readlines()
        assert content[-1] == "my_function ok 5"


def test_error_file():
    file_name = "test.txt"

    @log(filename=file_name)
    def my_function(x, y):
        return x + y

    with pytest.raises(TypeError):
        my_function(2, "3")

    with open(file_name, "r", encoding="utf-8") as f:
        content = f.readlines()
        assert content[-1] == "my_function error: <class 'TypeError'>. args: (2, '3'), kwargs: {}\n"
