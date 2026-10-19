stop_word = "стоп"
lis1= []
try:
    with open("words.txt","w", encoding="utf-8") as file:
        while True: 
                    word = input("Напишите заметку: \n")
                    if word == stop_word:
                        break
                    file.write(word + "\n")
    with open("words.txt","r", encoding="utf-8") as file:
        for word in file:
            lis1.append(word.strip())
    print(f"слов записано: {len(lis1)}")
except FileNotFoundError:
        print("Файл не найден\n")
