import os
import shutil
from pathlib import Path

RECIPE_BOOK_PATH = Path(Path.home(), "Data", "Recetas")


# functions
def select_option():
    print(
        "1: Read recipe\n"
        + "2: Create recipe\n"
        + "3: Create category\n"
        + "4: Remove recipe\n"
        + "5: Remove category\n"
        + "6: Exit\n"
    )
    election = input("Select a option: ")
    return election


def display_categories():
    print("Categories: ")
    for index, category in enumerate(Path(RECIPE_BOOK_PATH).glob("*/")):
        print(f"{index+1}. {category.stem}")


def select_category():
    category_selected = ""
    flag = False
    while flag == False:
        category_list = list(Path(RECIPE_BOOK_PATH).glob("*/"))
        if len(category_list):
            category_selected_index = input("Select a category(0 to cancel): ")
            for index, category in enumerate(category_list):
                if str(index + 1) == category_selected_index:
                    category_selected = category
                    flag = True
                    break
                elif category_selected_index == "0":
                    category_selected = 0
                    flag = True
                    break
            if flag == False:
                print("The number that you selected is invalid")
            return category_selected
        else:
            print("There are not categories")
            return -1


def display_recipies(category_selected):
    print("Recipies: ")
    for index, category in enumerate(
        Path(RECIPE_BOOK_PATH, category_selected).glob("*.txt")
    ):
        print(f"{index+1}. {category.stem}")


def select_recipe(category_selected):
    recipe_selected = ""
    flag = False
    recipe_list = list(Path(RECIPE_BOOK_PATH, category_selected).glob("*.txt"))
    if len(recipe_list) != 0:
        while flag == False:
            recipe_selected_index = input("Select a recipe(0 to cancel): ")
            for index, recipe in enumerate(
                Path(RECIPE_BOOK_PATH, category_selected).glob("*.txt")
            ):
                if str(index + 1) == recipe_selected_index:
                    recipe_selected = recipe
                    flag = True
                    break
                elif recipe_selected_index == "0":
                    recipe_selected = 0
                    flag = True
                    break
            if flag == False:
                print("The number that you selected is invalid")
        return recipe_selected
    else:
        print("There are not recipies")
        return -1


def read_recipe(category_selected, recipe_selected):
    path = Path(RECIPE_BOOK_PATH, category_selected, recipe_selected)
    file = open(path)
    print(file.read())
    file.close


def select_clear():
    # Wait for the user to press enter
    input("Press Enter to continue...")
    # Clear the console
    os.system("cls" if os.name == "nt" else "clear")


def clear():
    # Clear the console
    os.system("cls" if os.name == "nt" else "clear")


def create_category():
    category_to_create = input("Enter the new category: ")
    path = RECIPE_BOOK_PATH / category_to_create
    os.mkdir(path)


def create_recipe(category_selected):
    recipe_to_create = input("Enter the name of the new recipe: ") + ".txt"
    path = Path(RECIPE_BOOK_PATH, category_selected, recipe_to_create)
    file = open(path, "w")
    recipe = input("Enter the recipe instructions: ")
    file.write(recipe)
    file.close


def remove_recipe(category_selected, recipe_selected):
    path = RECIPE_BOOK_PATH / category_selected / recipe_selected
    os.remove(path)


def remove_category(category_selected):
    path = RECIPE_BOOK_PATH / category_selected
    shutil.rmtree(path)


# loop
election = 0
while election != 6:
    election = select_option()
    match election:
        case "1":
            # read recipe
            display_categories()
            category_selected = select_category()
            if category_selected != 0 and category_selected != -1:
                display_recipies(category_selected)
                recipe_selected = select_recipe(category_selected)
                if recipe_selected != 0 and recipe_selected != -1:
                    read_recipe(category_selected, recipe_selected)
                    select_clear()
                elif recipe_selected == -1:
                    select_clear()
                else:
                    clear()
            elif category_selected == -1:
                select_clear()
            else:
                clear()
        case "2":
            # create recipe
            display_categories()
            category_selected = select_category()
            if category_selected != 0 and category_selected != -1:
                create_recipe(category_selected)
                select_clear()
            elif category_selected != -1:
                select_clear()
            else:
                clear()
        case "3":
            # create category
            display_categories()
            create_category()
            select_clear()
        case "4":
            # remove recipe
            display_categories()
            category_selected = select_category()
            if category_selected != 0 and category_selected != -1:
                display_recipies(category_selected)
                recipe_selected = select_recipe(category_selected)
                if recipe_selected != 0 and recipe_selected != -1:
                    remove_recipe(category_selected, recipe_selected)
                    select_clear()
                elif recipe_selected == -1:
                    select_clear()
                else:
                    clear()
            elif category_selected == -1:
                select_clear()
            else:
                clear()
        case "5":
            # remove category
            display_categories()
            category_selected = select_category()
            if category_selected != 0 and category_selected != -1:
                remove_category(category_selected)
                select_clear()
            elif category_selected == -1:
                select_clear()
            else:
                clear()
        case "6":
            # end program
            break
        case _:
            print("That option doesn't exist")
