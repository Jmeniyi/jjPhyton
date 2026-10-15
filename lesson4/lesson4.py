
for i in range(1,11):
    print(i)

for i in range(2,21, 2):
      print(i)

total = 0

for i in range(1, 101):
    total += i
print(total)

word = input("Введите любое слово :")

for  letter in word:
    print(letter)

while True:
    password = input("Пароль: ")
    if password == "1234":
        print("Пароль верный")
        break
    print("повторите ещё раз")
