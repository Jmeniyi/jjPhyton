def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
                print("вводите только числа!")

def is_even(n):
    return n %2 == 0

if __name__ == "__main__":
    print(is_even(4))
    print(is_even(7))
    