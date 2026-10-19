def get_number(prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Ошибка. Вводите только числа")
        else:
            return number
        
age = get_number("Введите число: ")
print(f"Ваше число: {age}")


my_list = [1, 2, 3];
try: 
    print(my_list[5])
except IndexError as error:
    print(f"Такого значения нет в списке {error}")