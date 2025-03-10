import os

import services


def clean_screen():
    # Wait for the user to press enter
    input("Press Enter to continue...")
    # Clear the console
    os.system("cls" if os.name == "nt" else "clear")


def start():
    option = 0
    while option != 5:
        print(
            "Options:\n"
            "1. Perfumery\n"
            "2. Pharmacy\n"
            "3. Cosmetics\n"
            "4. Cancel\n"
            "5. Finish\n"
        )
        option = input("Where you wanna go? ")
        match option:
            case "1":
                services.decorator("P")
            case "2":
                services.decorator("F")
            case "3":
                services.decorator("C")
            case "4":
                print("You canceled your turn")
            case "5":
                print("Finish program")
                break
            case _:
                print("That is not a option")
        clean_screen()


start()
