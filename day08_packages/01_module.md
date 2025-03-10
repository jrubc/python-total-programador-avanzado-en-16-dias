# Installing packages

PyPi is a open-source repository:

```bash
pip install
```

It's recommendable to create a python environment and then install packages into it instead of installing the packages on your operating system.

# What is a module?

A module is code of python storaged in a python file (a file with extension .py)

# What is a package

A package is a group of modules

All packages need to have atleast a file called `__init__.py` is useful to python understand that is a package and not a common directory

# Create modules and packages

# Error handling

## Try

## Except

## Finally

# Error detecting using pylint

```python
def addition():
    n1 = int(input("number 1: "))
    n2 = int(input("number 2: "))
    print(n1 + n2)
    print("Thanks for addition" + n1)


try:
    addition()
except TypeError:
    # Code to run if there are a error
    print("You're trying concatenate different types of data")

except ValueError:
    print("You're trying to enter a string instead of a number")
else:
    print("All is fine")
    # Code to run if there are not a error
    pass
finally:
    print("That was all")
    # Code to run always
```

```python
def ask_for_a_number():

    while True:
        try:
            number = int(input("Give me a number: "))
        except:
            print("That is not a number")
        else:
            print(f"You entered the number {number}")
            break

    print("Thanks")


ask_for_a_number()
```
