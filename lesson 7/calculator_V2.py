print("===--Калькулятор-V2--===")
layer = "_" * 50
while True:
    try:
        c = int(input("1-Сложить 2-Отнять 3-Разделить 4-Умножить 0-Выход:"))

        if c == 0:
            print("Выход")
            print(layer)
            break

        if c not in (0, 1, 2, 3, 4):
            print("Нет такого пункта")
            print(layer)
            continue
        
        a = int(input("Первое число: "))
        b = int(input("Второе число: "))


        if c == 1:
            print(a+b)
            print(layer)
        elif c == 2:
            print(a-b)
            print(layer)
        elif c == 3:
            print(a/b)
            print(layer)
        elif c == 4:
            print(a*b)
            print(layer)
        elif c == 0:
            print("Выход")
            print(layer)
            break
    except ZeroDivisionError:
            print("На ноль делить нельзя")
            print(layer)
    except ValueError:
            print("Ошибка. Вводите только числа")
            print(layer)