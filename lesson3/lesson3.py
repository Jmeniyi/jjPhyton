ask_number_one = int(input("Введи первое число : "))
ask_number_two = int(input("Введи второе число: "))

if ask_number_one > ask_number_two:
    print(ask_number_one)
elif ask_number_one < ask_number_two:
    print(ask_number_two)
else: 
    print("числа равны")


ask_age = int(input("Введи возраст: "))

if ask_age < 12:
    print('ребёнок')
elif ask_age < 18 :
    print("подросток") 
elif ask_age < 65:
    print("взрослый")   
else:
    print("пенсионер")      

user_login = input("введите логин: ")
user_password = input ("введите пароль: ")

if user_login == "admin" and user_password == "1234":
    print("добро Пожаловать")
else:
    print("Неверный логин или пароль")
