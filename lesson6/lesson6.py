def say_hello(name):
    print(f"Привет, {name}")
say_hello("maksim")
say_hello("maksim2")
say_hello("maksim3")

def square(number):
   return  number * number
print(square(5), square(-3))


def get_max(a, b):
    if a > b:
        return a
    return b
print(get_max(5,7))

def get_age_category(age):
         if age < 12:
            return "ребёнок"
         elif age < 18:
             return "подросток"
         elif age < 65:
            return "взрослый"
         return "пенсионер"

for age in [11, 12, 17, 18, 64, 65]:
    print(age, get_age_category(age))


def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return(total)
print(sum_list([5,4,5,4,5]))


import math
def factorial(n):
    result = math.factorial(n)
    print(result)
factorial(5)



def fack(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
n = int(input("Введите число: "))
print(f"Факториал числа {n} равен {fack(n)}")