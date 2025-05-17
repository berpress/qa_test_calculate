from src.calc import calculate


def test_calc_division(): # тестирование деления
    assert calculate(10, 2, '/') == 5

def test_calc_subtraction(): # тестирование вычитания
    assert calculate(5, 2, '-') == 3

def test_calc_multiplication(): # тестирование умножение
    assert calculate(2, 2, '*') == 4

def test_calc_addition(): # тестирование cложение
    assert calculate(1, 2, '+') == 3
