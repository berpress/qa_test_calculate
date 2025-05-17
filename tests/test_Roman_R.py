print("Ну как там с деньгами?")

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
while True:
    action = input("Выберите действие (+ - * / q для выхода): ")
    if action.lower() == 'q':
        print("Денег нет, До свидания!")
        break
    try:
        if action == '+':
            result = a + b
        elif action == '-':
            result = a - b
        elif action == '*':
            result = a * b
        elif action == '/':
            result = a / b
        else:
            print("Неверное действие")

            continue
        print("Результат:", result)
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")
    except ValueError:
        print("Некорректный ввод. Повторите попытку.")