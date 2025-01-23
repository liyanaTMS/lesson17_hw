import pytest
from app.app import add, subtract, multiply, divide

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2,3,5),
        (-1,1,0),
        (0,0,0)
    ]
)
def test_add(a,b,expected):
    """Тестирует функцию сложения."""
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expect",
    [
        (10,2,5),
        (9,3,3)
    ]
)
def test_divide(a,b,expect):
    """Тестирует функцию деления."""
    assert divide(a, b) == expect


def test_divide_msg():
    """Тестирует вызов сообщения ValueError, если второй аргумент (b) равен нулю."""
    with pytest.raises(ValueError) as excinfo:
        divide(1, 0)
    assert str(excinfo.value) == "Деление на ноль невозможно"


@pytest.mark.parametrize(
    "a,b,expect",
    [
        (6,4,2),
        (-1,8,-9),
        (0,3,-3)
    ]
)
def test_subtract(a,b,expect):
    """Тестирует функцию вычитания."""
    assert subtract(a, b) == expect


@pytest.mark.parametrize(
    "a,b,expect",
    [
        (3,5,15),
        (8,-2,-16),
        (1,0,0)
    ]
)
def test_multiply(a,b,expect):
    """Тестирует функцию умножения."""
    assert multiply(a, b) == expect
