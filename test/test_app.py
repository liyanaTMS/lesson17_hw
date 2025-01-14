import pytest
from app.app import add, subtract, multiply, divide


def test_add():
    """Тестирует функцию сложения."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_divide():
    """Тестирует функцию деления."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3



def test_divide_msg():
    """
    Тестирует вызов сообщения ValueError, если второй аргумент (b) равен нулю.
    """
    with pytest.raises(ValueError) as excinfo:
        divide(1, 0)
    assert str(excinfo.value) == "Деление на ноль невозможно"


def test_subtract():
    """Тестирует функцию вычитания."""
    assert subtract(6, 4) == 2
    assert subtract(-1, 8) == -9
    assert subtract(0, 3) == -3


def test_multiply():
    """Тестирует функцию умножения."""
    assert multiply(3, 5) == 15
    assert multiply(8, -2) == -16
    assert multiply(1, 0) == 0