
try:
    with open("notes.txt","w", encoding="utf-8") as file:
        file.write("запись 1\n")
        file.write("запись 2\n")
        file.write("запись 3\n")

except FileNotFoundError:
    print("Файл ненайден")

with open("notes.txt","r", encoding="utf-8") as file:
        text = file.read()
        print(text)
with open("notes.txt","a", encoding="utf-8") as file:
        file.write("Запись через а")
with open ("notes.txt","r", encoding="utf-8") as file:
    for note in file:
        print(note.strip())

try:
     with open("notes1.txt","r", encoding="utf-8") as file:
        file.read()
except FileNotFoundError:
    print("Файл ненайден")

