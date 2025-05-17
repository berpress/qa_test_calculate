from src.calc import calculate

def test_add():
    """Cложение"""
    assert calculate(2, 2, '+') == 4

def test_sub():
    """Вычитание"""
    assert calculate(4, 6, '-') == -2  

def test_mult():
    """Умножение"""
    assert calculate(3, 2, '*') == 6

def test_div():
    """Деление"""
    assert calculate(5, 2, '/') == 2.5  

def test_div_0():
    """Деление на ноль"""
    assert calculate(3, 0, '/') == "Ошибка: деление на ноль!"

def test_inv():
    """Неверная операция"""
    assert calculate(1, 1, 'invalid') == "Неверная операция"