import random

while True:
    choice = input("Roll the dice? (y/n): ").lower()

    if choice == 'y':
        random_number = (random.randint(1,6), random.randint(1,6))
        print(random_number)
    elif choice == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid Choice!")