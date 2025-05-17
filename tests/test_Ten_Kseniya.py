from src.calc import calculate


def test_calc_division(): # тестирование деления
    assert calculate(124, 2, '/') == 62

def test_calc_subtraction(): # тестирование вычитания
    assert calculate(876, 321, '-') == 555

def test_calc_multiplication(): # тестирование умножение
    assert calculate(246, 2, '*') == 492

def test_calc_addition(): # тестирование cложение
    assert calculate(987, 123, '+') == 1110