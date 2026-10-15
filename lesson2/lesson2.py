name = input("Как тебя зовут? ")
city = input("Из какого ты города? ")
name = name.capitalize()
city = city.title()
word = input("любое слово")
age = int(input("ваш возраст?: " ))

numberOne= int(input("певое число"))
numberTwo= int(input("второе число"))

summ = numberOne + numberTwo

total = numberOne + numberTwo

year = int(2026)

print(f"Привет, {name}, из города {city}!")
print(f"сумма {numberOne}, и {numberTwo} = {summ}")
print(f"{numberOne}+{numberTwo} = {summ}")
print(f"длина строки {word} = {len(word)}")
print(f"первая буква строки {word[0]}, а последняя {word[-1]}")
print(f"слово на оборот {word[::-1]}")
print(f"вы родились в {year-age} году")