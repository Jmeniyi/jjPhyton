print("===--Калькулятор-V3--===")
import calculator_v3_tool as history
layer = "_" * 50

while True:
    try:
        c = int(input("1-Сложить 2-Отнять 3-Разделить 4-Умножить " 
        "5-история вычислений 0-Выход:"))

        if c == 0:
            print("Выход")
            print(layer)
            break

        if c == 5:
            with open("story_Calculator.txt", "r", encoding="utf-8") as file:
                story = file.read()
                if story:
                    print(story)
                else:
                    print("История пуста")
                continue

        if c not in (0, 1, 2, 3, 4,5):
            print("Нет такого пункта")
            print(layer)
            continue
        
        a = int(input("Первое число: "))
        b = int(input("Второе число: "))


        if c == 1:
            summ = a+b
            print(summ)
            history.save_to_history(f"{a} + {b} = {summ}\n")
            print(layer)

        elif c == 2:
            difference = a-b
            print(a-b)
            history.save_to_history(f"{a} - {b} = {difference}\n")
            print(layer)

        elif c == 3:
            divide = a/b
            print(a/b)
            history.save_to_history(f"{a} / {b} = {divide}\n")
            print(layer)
        elif c == 4:
            multyply = a*b
            print(a*b)
            history.save_to_history(f"{a} * {b} = {multyply}\n")
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
    except FileNotFoundError:
        print("История пока пуста")
            