print("===--Угадай число--===")

import random
secret_Number = random.randint(1,100)
count_try = 0


while True:
    try:
        user_number = int(input("Введите число от 1 до 100: "))
        count_try+=1

        if not 1 <= user_number <= 100:
            print("Введите число от 1 до 100")
            continue
        if user_number > secret_Number:
            print("Ваше число больше загаданного")
        elif user_number < secret_Number:
            print("Ваше число меньше загаданного")
        else: 
            print(f"Поздравляем! ВЫ угадали \n Это цифра: {secret_Number}\n Попыток произведено:  {count_try}")
            break
    except ValueError:
        print("вводите только числа!")

