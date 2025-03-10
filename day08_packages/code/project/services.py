# services.py


# Generators
def perfumery_generator():
    turn = 0
    while True:
        turn += 1
        yield f"P{turn}"


def pharmacy_generator():
    turn = 0
    while True:
        turn += 1
        yield f"F{turn}"


def cosmetics_generator():
    turn = 0
    while True:
        turn += 1
        yield f"C{turn}"


# Create generator instances
p = perfumery_generator()
f = pharmacy_generator()
c = cosmetics_generator()


# Decorators
def decorate_generator():
    # Based on the area, choose the correct generator
    def decorator(area):
        print("Hello! your turn is:")

        # Choose the generator based on the area
        if area == "P":
            print(next(p))  # Perfumery
        elif area == "F":
            print(next(f))  # Pharmacy
        elif area == "C":
            print(next(c))  # Cosmetics
        else:
            print("Invalid area")  # In case of an invalid area

        print("Please, wait and you will be assisted")

    return decorator


decorator = decorate_generator()
