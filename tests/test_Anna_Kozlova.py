from src.calc import calculate

def test_calc_division(): # тестирование деления
    assert calculate(18, 3, '/') == 6

def test_calc_subtraction(): # тестирование вычитания
    assert calculate(18, 3, '-') == 15

def test_calc_multiplication(): # тестирование умножение
    assert calculate(18, 3, '*') == 54

def test_calc_addition(): # тестирование cложение
    assert calculate(18, 3, '+') == 21
