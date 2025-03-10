import datetime
import random
from tkinter import (
    BOTTOM,
    CENTER,
    DISABLED,
    END,
    FLAT,
    LEFT,
    NORMAL,
    RIGHT,
    TOP,
    Button,
    Checkbutton,
    Entry,
    Frame,
    IntVar,
    Label,
    LabelFrame,
    N,
    StringVar,
    Text,
    Tk,
    W,
    filedialog,
    messagebox,
)

from constantes import *

operator = ""


def click_button(number):
    global operator
    operator += number
    calculator_viewer.delete(0, END)
    calculator_viewer.insert(END, operator)


def delete():
    global operator
    operator = ""
    calculator_viewer.delete(0, END)


def get_result():
    global operator
    result = str(eval(operator))
    calculator_viewer.delete(0, END)
    calculator_viewer.insert(END, result)


def create_cost_boxes(category, row, column):
    # Cost panel labels and entries
    label = Label(
        costs_panel,
        text=category,
        font=("Dosis", 12, "bold"),
        bg="#262D33",
        fg="#A1A8B6",
    )
    label.grid(row=row, column=column)

    box_content = StringVar()
    box = Entry(
        costs_panel,
        font=("Dosis", 12, "bold"),
        bd=1,
        width=10,
        state="readonly",
        textvariable=box_content,
    )
    box.grid(row=row, column=column + 1)
    return box_content


def create_checks(panel, item_list):
    """
    Create the check buttons and storage for their activation state.

    The check buttons indicate if the customer asks for a specific meal, drink, or dessert.
    Each check button is paired with an entry box to store additional information.

    Parameters:
    - panel: The parent widget where the check buttons and entry boxes will be placed.
    - item_list: A list of items (e.g., meals, drinks, desserts) to create check buttons for.

    Returns:
    - variables: A list of IntVar objects representing the state of each check button.
    - boxes_content: A list of StringVar objects representing the content of each entry box.
    """
    boxes = (
        []
    )  # Graphic elements boxes_content = []  # Logic variables for entry contents
    variables = []  # Logic variables for check button contents
    boxes_content = []
    for index, item in enumerate(item_list):
        var = IntVar()
        chk_button = Checkbutton(
            panel,
            anchor=W,
            text=item.title(),
            bg="#262D33",
            fg="#A1A8B6",
            font=("Dosis", 19, "bold"),
            onvalue=1,
            offvalue=0,
            variable=var,
            command=check_buttons,
            width=9,
        )
        variables.append(var)
        chk_button.grid(row=index, column=0, sticky=W)

        box_content = StringVar()
        box_content.set("0")
        box = Entry(
            panel,
            font=("Dosis", 19, "bold"),
            bd=1,
            bg="#262D33",
            fg="#A1A8B6",
            width=6,
            state=DISABLED,
            textvariable=box_content,
        )
        boxes.append(box)
        boxes_content.append(box_content)
        box.grid(row=index, column=1, sticky=W)
    return variables, boxes, boxes_content


def create_labelframe_panels(category):
    """
    Create the panels for Meal, Drink and Dessert
    """
    # Meal, Drink, Dessert Panels
    panel = LabelFrame(
        left_panel,
        labelanchor=N,
        text=category,
        font=("Dosis", 19, "bold"),
        bd=1,
        bg="#262D33",
        relief=FLAT,
        fg="#A1A8B6",
    )
    panel.pack(side=LEFT, expand=True)
    return panel


def create_panel(parent, side, padx=0, pady=0):
    """
    Create main and sub panels
    """
    panel = Frame(parent, bd=1, relief=FLAT, bg="#262D33", padx=padx, pady=pady)
    panel.pack(side=side)
    return panel


def check_buttons():
    for index in range(len(meal_boxes)):
        # Use a helper function to avoid repetition
        toggle_box_state(
            meal_variables[index], meal_boxes[index], meal_boxes_content[index]
        )
        toggle_box_state(
            drink_variables[index], drink_boxes[index], drink_boxes_content[index]
        )
        toggle_box_state(
            dessert_variables[index], dessert_boxes[index], dessert_boxes_content[index]
        )


def toggle_box_state(variable, box, box_content):
    """Helper function to enable or disable a box based on the variable's state."""
    if variable.get() == 1:
        box.config(state=NORMAL)  # Enable the box
        if box.get() == "0":
            box.delete(0, END)
        box.focus()
    else:
        box.config(state=DISABLED)  # Disable the box
        box_content.set("0")


def calculate_subtotal(boxes_content, prices):
    """Helper function to calculate the subtotal for a given category."""
    subtotal = 0
    for index, amount in enumerate(boxes_content):
        subtotal += float(amount.get()) * prices[index]
    return subtotal


def total():
    # Calculate subtotals for each category
    sub_total_meal = calculate_subtotal(meal_boxes_content, MEAL_PRICES)
    sub_total_drink = calculate_subtotal(drink_boxes_content, DRINK_PRICES)
    sub_total_dessert = calculate_subtotal(dessert_boxes_content, DESSERT_PRICES)

    # Calculate total, taxes, etc.
    sub_total = sub_total_meal + sub_total_drink + sub_total_dessert
    taxes = sub_total * 0.07
    total_cost = sub_total + taxes

    # Update the display variables
    meal_cost_var.set(f"$ {round(sub_total_meal, 2)}")
    drink_cost_var.set(f"$ {round(sub_total_drink, 2)}")
    dessert_cost_var.set(f"$ {round(sub_total_dessert, 2)}")
    subtotal_var.set(f"$ {round(sub_total, 2)}")
    taxes_var.set(f"$ {round(taxes, 2)}")
    total_var.set(f"$ {round(total_cost, 2)}")


def receipt():
    receipt_content.delete(1.0, END)
    receipt_num = f"N# - {random.randint(1000, 9999)}"
    date = datetime.datetime.now()
    receipt_date = f"{date.day}/{date.month}/{date.year} - {date.hour}:{date.minute}"
    receipt_content.insert(END, f"Dates:\t{receipt_num}\t\t{receipt_date}\n")
    receipt_content.insert(END, f"*" * 40 + "\n")
    receipt_content.insert(END, "Items\t\tAmount\tItems cost\n")
    receipt_content.insert(END, f"-" * 54 + "\n")

    x = 0
    for meal in meal_boxes_content:
        if meal.get() != "0":
            receipt_content.insert(
                END,
                f"{MEAL_LIST[x]}\t\t{meal.get()}\t$ {int(meal.get())*MEAL_PRICES[x]}\n",
            )
        x += 1

    x = 0
    for drink in drink_boxes_content:
        if drink.get() != "0":
            receipt_content.insert(
                END,
                f"{DRINK_LIST[x]}\t\t{drink.get()}\t$ {int(drink.get())*DRINK_PRICES[x]}\n",
            )
        x += 1

    x = 0
    for dessert in dessert_boxes_content:
        if dessert.get() != "0":
            receipt_content.insert(
                END,
                f"{DESSERT_LIST[x]}\t\t{dessert.get()}\t$ {int(dessert.get())*DESSERT_PRICES[x]}\n",
            )
        x += 1
    receipt_content.insert(END, f"-" * 54 + "\n")
    receipt_content.insert(END, f" Costo de la Comida: \t\t\t{meal_cost_var.get()}\n")
    receipt_content.insert(END, f" Costo de la Bebida: \t\t\t{drink_cost_var.get()}\n")
    receipt_content.insert(
        END, f" Costo de la Postres: \t\t\t{dessert_cost_var.get()}\n"
    )
    receipt_content.insert(END, f"-" * 54 + "\n")
    receipt_content.insert(END, f" Sub-total: \t\t\t{subtotal_var.get()}\n")
    receipt_content.insert(END, f" Impuestos: \t\t\t{taxes_var.get()}\n")
    receipt_content.insert(END, f" Total: \t\t\t{total_var.get()}\n")
    receipt_content.insert(END, f"*" * 47 + "\n")
    receipt_content.insert(END, "Lo esperamos pronto")


def save():
    info_recibo = receipt_content.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if archivo != None:
        archivo.write(info_recibo)
        archivo.close()
    messagebox.showinfo("Informacion", "Su recibo ha sido guardado")


def reset():
    receipt_content.delete(0.1, END)

    for text in meal_boxes_content:
        text.set("0")
    for text in drink_boxes_content:
        text.set("0")
    for text in dessert_boxes_content:
        text.set("0")

    for cuadro in meal_boxes:
        cuadro.config(state=DISABLED)
    for cuadro in drink_boxes:
        cuadro.config(state=DISABLED)
    for cuadro in dessert_boxes:
        cuadro.config(state=DISABLED)

    for v in meal_variables:
        v.set(0)
    for v in drink_variables:
        v.set(0)
    for v in dessert_variables:
        v.set(0)

    meal_cost_var.set("")
    drink_cost_var.set("")
    dessert_cost_var.set("")
    subtotal_var.set("")
    taxes_var.set("")
    total_var.set("")


# MAIN WINDOW SETUP

# initialize tkinter
app = Tk()

# window size
app.geometry("1274x615")

# prevent maximize
app.resizable(False, False)

# title
app.title("Menu")

# background
app.config(bg="#0C1017")


# Main panels
top_panel = create_panel(app, side=TOP, padx=15)
left_panel = create_panel(app, side=LEFT)
right_panel = create_panel(app, side=RIGHT)

# Sub panels
costs_panel = create_panel(parent=left_panel, side=BOTTOM, padx=0, pady=20)
calculator_panel = create_panel(parent=right_panel, side=TOP)
receipt_panel = create_panel(parent=right_panel, side=TOP)
buttons_panel = create_panel(parent=right_panel, side=BOTTOM)

# tag title
title_tag = Label(
    top_panel,
    text="Fracture System",
    fg="#A1A8B6",
    font=("Dosis", 58),
    bg="#262D33",
    width=28,
)

title_tag.grid(row=0, column=0)

# Create Meal, Drink and Dessert panels
meal_panel = create_labelframe_panels(category="Meal")
drink_panel = create_labelframe_panels(category="Drink")
dessert_panel = create_labelframe_panels(category="Dessert")

# Create Meal, Drink and Dessert check buttons and entry items
meal_variables, meal_boxes, meal_boxes_content = create_checks(meal_panel, MEAL_LIST)
drink_variables, drink_boxes, drink_boxes_content = create_checks(
    drink_panel, DRINK_LIST
)
dessert_variables, dessert_boxes, dessert_boxes_content = create_checks(
    dessert_panel, DESSERT_LIST
)

# Create Costs panel content (labels and entries)
meal_cost_var = create_cost_boxes("Meal Cost", row=0, column=0)
drink_cost_var = create_cost_boxes("Drink Cost", row=1, column=0)
dessert_cost_var = create_cost_boxes("Dessert Cost", row=2, column=0)
subtotal_var = create_cost_boxes("Subtotal", row=0, column=2)
taxes_var = create_cost_boxes("Taxes", row=1, column=2)
total_var = create_cost_boxes("Total", row=2, column=2)

# Create Buttons
buttons = ["total", "receipt", "save", "reset"]
saves_especial_buttons = []
for index, button in enumerate(buttons):
    button = Button(
        buttons_panel,
        text=button.title(),
        fg="#A1A8B6",
        font=("Dosis", 14, "bold"),
        bg="#262D33",
        bd=1,
        width=7,
    )
    saves_especial_buttons.append(button)
    button.grid(row=0, column=index)

saves_especial_buttons[0].config(command=total)
saves_especial_buttons[1].config(command=receipt)
saves_especial_buttons[2].config(command=save)
saves_especial_buttons[3].config(command=reset)

# Create Receipt
receipt_content = Text(
    receipt_panel, font=("Dosis", 12, "bold"), bd=1, width=46, height=10
)
receipt_content.grid(row=0, column=0)

# Create viewer calculator
calculator_viewer = Entry(calculator_panel, font=("Dosis", 16, "bold"), width=34, bd=1)
calculator_viewer.grid(row=0, column=0, columnspan=4)

calculator_buttons = [
    "7",
    "8",
    "9",
    "+",
    "4",
    "5",
    "6",
    "-",
    "1",
    "2",
    "3",
    "*",
    "CE",
    "Clear",
    "0",
    "/",
]

saved_buttons = []

for index, button in enumerate(calculator_buttons):
    row = index // 4 + 1
    column = index % 4
    button = Button(
        calculator_panel,
        text=button.title(),
        font=("Dosis", 16, "bold"),
        fg="white",
        bg="azure4",
        bd=1,
        width=6,
    )
    saved_buttons.append(button)

    button.grid(row=row, column=column, sticky="nsew")

button_commands = [
    ("7", "8", "9", "+"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "*"),
    ("0", "/", None, None),  # Assuming the last two buttons are for result and clean
]

# Loop through button_commands and assign them to saved_buttons
for i, row in enumerate(button_commands):
    for j, command in enumerate(row):
        if command:
            saved_buttons[i * 4 + j].config(
                command=lambda cmd=command: click_button(cmd)
            )

# Specific buttons for result and clear
saved_buttons[12].config(command=get_result)
saved_buttons[13].config(command=delete)
app.mainloop()
