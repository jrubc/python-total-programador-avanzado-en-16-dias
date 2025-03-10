import datetime
import random
from tkinter import (BOTTOM, DISABLED, END, FLAT, LEFT, NORMAL, RIGHT, TOP,
                     Button, Checkbutton, Entry, Frame, IntVar, Label,
                     LabelFrame, StringVar, Text, Tk, W, filedialog,
                     messagebox)

operator = ""
meal_prices = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
drink_prices = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
dessert_prices = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_button(number):
    global operator
    operator = operator + number
    calculator_viewer.delete(0, END)
    calculator_viewer.insert(END, operator)


def clean():
    global operator
    operator = ""
    calculator_viewer.delete(0, END)


def get_result():
    global operator
    result = str(eval(operator))
    calculator_viewer.delete(0, END)
    calculator_viewer.insert(0, result)
    operator = ""


def check_buttons():
    for x in range(len(meal_frames)):
        if meal_variables[x].get() == 1:
            meal_frames[x].config(state=NORMAL)
            if meal_frames[x].get() == "0":
                meal_frames[x].delete(0, END)
            meal_frames[x].focus()
        else:
            meal_frames[x].config(state=DISABLED)
            meal_text[x].set("0")

    for x in range(len(drink_frames)):
        if drink_variables[x].get() == 1:
            drink_frames[x].config(state=NORMAL)
            if drink_frames[x].get() == "0":
                drink_frames[x].delete(0, END)
            drink_frames[x].focus()
        else:
            drink_frames[x].config(state=DISABLED)
            drink_text[x].set("0")

    for x in range(len(dessert_frames)):
        if dessert_variables[x].get() == 1:
            dessert_frames[x].config(state=NORMAL)
            if dessert_frames[x].get() == "0":
                dessert_frames[x].delete(0, END)
            dessert_frames[x].focus()
        else:
            dessert_frames[x].config(state=DISABLED)
            dessert_text[x].set("0")


def total():
    sub_total_meal = 0
    p = 0
    for amount in meal_text:
        sub_total_meal = sub_total_meal + (float(amount.get()) * meal_prices[p])
        p += 1

    sub_total_drink = 0
    p = 0
    for amount in drink_text:
        sub_total_drink = sub_total_drink + (float(amount.get()) * drink_prices[p])
        p += 1

    sub_total_dessert = 0
    p = 0
    for amount in dessert_text:
        sub_total_dessert = sub_total_dessert + (
            float(amount.get()) * dessert_prices[p]
        )
        p += 1

    sub_total = sub_total_meal + sub_total_drink + sub_total_dessert
    taxes = sub_total * 0.07
    total = sub_total + taxes

    meal_cost_var.set(f"$ {round(sub_total_meal, 2)}")
    drink_cost_var.set(f"$ {round(sub_total_drink, 2)}")
    dessert_cost_var.set(f"$ {round(sub_total_dessert, 2)}")
    subtotal_var.set(f"$ {round(sub_total, 2)}")
    tax_var.set(f"$ {round(taxes, 2)}")
    total_var.set(f"$ {round(total, 2)}")


def receipt():
    receipt_text.delete(1.0, END)
    receipt_num = f"N# - {random.randint(1000, 9999)}"
    date = datetime.datetime.now()
    receipt_date = f"{date.day}/{date.month}/{date.year} - {date.hour}:{date.minute}"
    receipt_text.insert(END, f"Dates:\t{receipt_num}\t\t{receipt_date}\n")
    receipt_text.insert(END, f"*" * 40 + "\n")
    receipt_text.insert(END, "Items\t\tAmount\tItems cost\n")
    receipt_text.insert(END, f"-" * 54 + "\n")

    x = 0
    for meal in meal_text:
        if meal.get() != "0":
            receipt_text.insert(
                END,
                f"{meal_list[x]}\t\t{meal.get()}\t$ {int(meal.get())*meal_prices[x]}\n",
            )
        x += 1

    x = 0
    for drink in drink_text:
        if drink.get() != "0":
            receipt_text.insert(
                END,
                f"{drink_list[x]}\t\t{drink.get()}\t$ {int(drink.get())*drink_prices[x]}\n",
            )
        x += 1

    x = 0
    for dessert in dessert_text:
        if dessert.get() != "0":
            receipt_text.insert(
                END,
                f"{dessert_list[x]}\t\t{dessert.get()}\t$ {int(dessert.get())*dessert_prices[x]}\n",
            )
        x += 1
    receipt_text.insert(END, f"-" * 54 + "\n")
    receipt_text.insert(END, f" Costo de la Comida: \t\t\t{meal_cost_var.get()}\n")
    receipt_text.insert(END, f" Costo de la Bebida: \t\t\t{drink_cost_var.get()}\n")
    receipt_text.insert(END, f" Costo de la Postres: \t\t\t{dessert_cost_var.get()}\n")
    receipt_text.insert(END, f"-" * 54 + "\n")
    receipt_text.insert(END, f" Sub-total: \t\t\t{subtotal_var.get()}\n")
    receipt_text.insert(END, f" Impuestos: \t\t\t{tax_var.get()}\n")
    receipt_text.insert(END, f" Total: \t\t\t{total_var.get()}\n")
    receipt_text.insert(END, f"*" * 47 + "\n")
    receipt_text.insert(END, "Lo esperamos pronto")


def save():
    info_recibo = receipt_text.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if archivo != None:
        archivo.write(info_recibo)
        archivo.close()
    messagebox.showinfo("Informacion", "Su recibo ha sido guardado")


def reset():
    receipt_text.delete(0.1, END)

    for text in meal_text:
        text.set("0")
    for text in drink_text:
        text.set("0")
    for text in dessert_text:
        text.set("0")

    for cuadro in meal_frames:
        cuadro.config(state=DISABLED)
    for cuadro in drink_frames:
        cuadro.config(state=DISABLED)
    for cuadro in dessert_frames:
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
    tax_var.set("")
    total_var.set("")


# Initialize tkinter
app = Tk()

# Window size
app.geometry("1270x630+0+0")

# Prevent maximize
app.resizable(False, False)

# Title
app.title("Say Drake, I hear you like 'em young")

# Background color
app.config(bg="burlywood")

# Top panel
top_panel = Frame(app, bd=1, relief=FLAT)
top_panel.pack(side=TOP)

# Tag title
title_tag = Label(
    top_panel,
    text="Facture System",
    fg="azure4",
    font=("Dosis", 58),
    bg="burlywood",
    width=27,
)
title_tag.grid(row=0, column=0)

# Left tag
left_panel = Frame(app, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# Costs panel
costs_panel = Frame(left_panel, bd=1, relief=FLAT, bg="azure4", padx=100)
costs_panel.pack(side=BOTTOM)

# Food panel
meal_panel = LabelFrame(
    left_panel, text="Food", font=("Dosis", 19, "bold"), bd=1, relief=FLAT, fg="azure4"
)
meal_panel.pack(side=LEFT)

# Drinks panel
drink_panel = LabelFrame(
    left_panel,
    text="Drinks",
    font=("Dosis", 19, "bold"),
    bd=1,
    relief=FLAT,
    fg="azure4",
)
drink_panel.pack(side=LEFT)

# Desserts panel
dessert_panel = LabelFrame(
    left_panel,
    text="Desserts",
    font=("Dosis", 19, "bold"),
    bd=1,
    relief=FLAT,
    fg="azure4",
)
dessert_panel.pack(side=LEFT)

# Right panel
right_panel = Frame(app, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# Calculator
calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
calculator_panel.pack()

# Receipt
receipt_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
receipt_panel.pack()

# Button
buttons_panel = Frame(right_panel, bd=1, relief=FLAT, bg="burlywood")
buttons_panel.pack()

# Products list
meal_list = [
    "chicken",
    "lamb",
    "salmon",
    "kebab",
    "pizza1",
    "pizza2",
    "pizza3",
    "pizza4",
]
drink_list = ["water", "soda", "cola", "juice", "wine1", "wine2", "wine3", "wine4"]
dessert_list = [
    "ice cream",
    "fruit",
    "brownies",
    "flan",
    "mousse",
    "cake1",
    "cake1",
    "cake1",
]

# Generate meal items
meal_variables = []
meal_frames = []
meal_text = []
count = 0

for meal in meal_list:
    # Create checkbutton
    meal_variables.append("")
    meal_variables[count] = IntVar()
    meal = Checkbutton(
        meal_panel,
        text=meal.title(),
        font=("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=meal_variables[count],
        command=check_buttons,
    )
    meal.grid(row=count, column=0, sticky=W)

    # Create input frames
    meal_frames.append("")
    meal_text.append("")
    meal_text[count] = StringVar()
    meal_text[count].set("0")
    meal_frames[count] = Entry(
        meal_panel,
        font=("Dosis", 18, "bold"),
        bd=1,
        width=6,
        state=DISABLED,
        textvariable=meal_text[count],
    )
    meal_frames[count].grid(row=count, column=1)
    count += 1

drink_variables = []
drink_frames = []
drink_text = []
count = 0

for drink in drink_list:
    # Create checkbutton
    drink_variables.append("")
    drink_variables[count] = IntVar()
    drink = Checkbutton(
        drink_panel,
        text=drink.title(),
        font=("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=drink_variables[count],
        command=check_buttons,
    )
    drink.grid(row=count, column=0, sticky=W)

    # Create input frames
    drink_frames.append("")
    drink_text.append("")
    drink_text[count] = StringVar()
    drink_text[count].set("0")
    drink_frames[count] = Entry(
        drink_panel,
        font=("Dosis", 18, "bold"),
        bd=1,
        width=6,
        state=DISABLED,
        textvariable=drink_text[count],
    )
    drink_frames[count].grid(row=count, column=1)
    count += 1

dessert_variables = []
dessert_frames = []
dessert_text = []
count = 0

for dessert in dessert_list:
    # Create checkbutton
    dessert_variables.append("")
    dessert_variables[count] = IntVar()
    dessert = Checkbutton(
        dessert_panel,
        text=dessert.title(),
        font=("Dosis", 19, "bold"),
        onvalue=1,
        offvalue=0,
        variable=dessert_variables[count],
        command=check_buttons,
    )
    dessert.grid(row=count, column=0, sticky=W)

    # Create input frames
    dessert_frames.append("")
    dessert_text.append("")
    dessert_text[count] = StringVar()
    dessert_text[count].set("0")
    dessert_frames[count] = Entry(
        dessert_panel,
        font=("Dosis", 18, "bold"),
        bd=1,
        width=6,
        state=DISABLED,
        textvariable=dessert_text[count],
    )
    dessert_frames[count].grid(row=count, column=1)
    count += 1

# variable list
meal_cost_var = StringVar()
drink_cost_var = StringVar()
dessert_cost_var = StringVar()
subtotal_var = StringVar()
tax_var = StringVar()
total_var = StringVar()

# cost tags and input fields
meal_cost_tag = Label(
    costs_panel, text="Meal cost", font=("Dosis", 12, "bold"), bg="azure4", fg="white"
)
meal_cost_tag.grid(row=0, column=0)

meal_cost_text = Entry(
    costs_panel,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=meal_cost_var,
)
meal_cost_text.grid(row=0, column=1)

# cost tags and input fields
drink_cost_tag = Label(
    costs_panel, text="Drink cost", font=("Dosis", 12, "bold"), bg="azure4", fg="white"
)
drink_cost_tag.grid(row=1, column=0)

drink_cost_text = Entry(
    costs_panel,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=drink_cost_var,
)
drink_cost_text.grid(row=1, column=1, padx=41)

# cost tags and input fields
dessert_cost_tag = Label(
    costs_panel,
    text="Dessert cost",
    font=("Dosis", 12, "bold"),
    bg="azure4",
    fg="white",
)
dessert_cost_tag.grid(row=2, column=0)

dessert_cost_text = Entry(
    costs_panel,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=dessert_cost_var,
)
dessert_cost_text.grid(row=2, column=1, padx=41)

# cost tags and input fields
subtotal_tag = Label(
    costs_panel,
    text="Subtotal",
    font=("Dosis", 12, "bold"),
    bg="azure4",
    fg="white",
)
subtotal_tag.grid(row=0, column=2)

subtotal_text = Entry(
    costs_panel,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=subtotal_var,
)
subtotal_text.grid(row=0, column=3, padx=41)

# cost tags and input fields
tax_tag = Label(
    costs_panel,
    text="Taxes",
    font=("Dosis", 12, "bold"),
    bg="azure4",
    fg="white",
)
tax_tag.grid(row=1, column=2)

tax_text = Entry(
    costs_panel,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=tax_var,
)
tax_text.grid(row=1, column=3, padx=41)

# cost tags and input fields
total_tag = Label(
    costs_panel,
    text="Total",
    font=("Dosis", 12, "bold"),
    bg="azure4",
    fg="white",
)
total_tag.grid(row=2, column=2)

total_text = Entry(
    costs_panel,
    font=("Dosis", 12, "bold"),
    bd=1,
    width=10,
    state="readonly",
    textvariable=total_var,
)
total_text.grid(row=2, column=3, padx=41)

# buttons
buttons = ["total", "receive", "save", "reset"]
created_buttons = []

columns = 0
for button in buttons:
    button = Button(
        buttons_panel,
        text=button.title(),
        font=("Dosis", 14, "bold"),
        fg="white",
        bg="azure4",
        bd=1,
        width=9,
    )

    created_buttons.append(button)
    button.grid(row=0, column=columns)
    columns += 1

created_buttons[0].config(command=total)
created_buttons[1].config(command=receipt)
created_buttons[2].config(command=save)
created_buttons[3].config(command=reset)

# receive area
receipt_text = Text(
    receipt_panel, font=("Dosis", 12, "bold"), bd=1, width=42, height=10
)
receipt_text.grid(row=0, column=0)

# Calculator
calculator_viewer = Entry(calculator_panel, font=("Dosis", 16, "bold"), width=32, bd=1)
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
    "x",
    "CE",
    "Borrar",
    "0",
    "/",
]

saved_buttons = []

row = 1
column = 0
for button in calculator_buttons:
    button = Button(
        calculator_panel,
        text=button.title(),
        font=("Dosis", 16, "bold"),
        fg="white",
        bg="azure4",
        bd=1,
        width=8,
    )
    saved_buttons.append(button)

    button.grid(row=row, column=column)
    if column == 3:
        row += 1

    column += 1

    if column == 4:
        column = 0

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
saved_buttons[13].config(command=clean)

# Prevent the window from closing
app.mainloop()
