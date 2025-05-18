# print("Ну как там с деньгами?")
#
# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))
# while True:
#     action = input("Выберите действие (+ - * / q для выхода): ")
#     if action.lower() == 'q':
#         print("Денег нет, До свидания!")
#         break
#     try:
#         if action == '+':
#             result = a + b
#         elif action == '-':
#             result = a - b
#         elif action == '*':
#             result = a * b
#         elif action == '/':
#             result = a / b
#         else:
#             print("Неверное действие")
#
#             continue
#         print("Результат:", result)
#     except ZeroDivisionError:
#         print("Делить на ноль нельзя!")
#     except ValueError:
#         print("Некорректный ввод. Повторите попытку.")

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