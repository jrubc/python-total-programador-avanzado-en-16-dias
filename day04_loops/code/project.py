from random import randint

# Generate magic number
magic_number = randint(0, 100)

# Lifes
lifes = 8

# Enter number
user_number = int(input("Enter a number between 0 and 100: "))
while lifes > 0:
    if user_number >= 0 and user_number <= 100:
        if user_number == magic_number:
            break
        elif user_number < magic_number:
            print(f"Your number {user_number} is minor than the magic number")
        elif user_number > magic_number:
            print(f"Your number {user_number} is major than the magic number")
        lifes -= 1
        if lifes != 0:
            print(f"lifes: {lifes}")
            user_number = int(input("Enter a number between 0 and 100: "))
    else:
        user_number = int(input("Enter a number between 0 and 100: "))

if lifes > 0:
    print(f"Congratulations you found the magic number ({magic_number})")
else:
    print(f"You're a fool and don't have lifes, the magic number was ({magic_number})")
