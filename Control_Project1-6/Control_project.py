print("===--Калькулятор--===")
while True:

    a = int(input(""))
    c = int(input("1-Сложить 2-Отнять 3-Разделить 4-Умножить 0-Выход:"))
    layer = "______________________________________________________________"
    if c == 0:
        print("Выход")
        print(layer)
        break

    b = int(input(""))


    if c == 1:
        print(a+b)
        print(layer)
    elif c == 2:
        print(a-b)
        print(layer)
    elif c == 3:
        if  c == 3 and b == 0:
                print("На ноль делить нельзя")
                print(layer)
                break
        else:
            print(a/b)
            print(layer)
    elif c == 4:
        print(a*b)
        print(layer)
    else:
        print("Нет такого пункта")
        print(layer)



