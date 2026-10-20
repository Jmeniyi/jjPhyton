from math import ceil, pi
import my_tools as tool 
from datetime import datetime
import requests

def area_of_circle():
    print("Считаем площадь круга")
    while True:
        radius = tool.get_number("Введите число:")
        if radius < 0:
            print("Радиус не может быть отрицательным")
        else:
            area = pi * radius ** 2
            print(f"Площадь круга: {ceil(area)}")
            break

#area_of_circle()

dt = datetime.now()
print(dt.strftime("%d.%m.%Y %H:%M"))

print(requests.__version__)