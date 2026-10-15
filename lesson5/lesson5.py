numbers = [
    1,2,3,4,5
]
print(len(numbers), numbers[0], numbers[-1], sum(numbers),max(numbers))
numbers.append(77)
numbers.remove(5)
print(numbers)

for num in numbers:
     if num %2 == 0:
        print(num)

user ={
    "name":"Eugen",
    "age":25,
    "city":"Krasnodar"
}

for key, value in user.items(): 
    print(f"{key}: {value}")

user["hobby"] = "Music"
user["age"] = 26
print(user)

print(user.get("likes", "значение не указано"))

words = []

while True :
    word = input("Ввидите слово: ")
    if word =="стоп":
        break
    else: 
        words.append(word)
print(words, len(words))