# Pyling

Run "python file.py -r y" to watch a report of your code
For example, a good code:

```python
"""
This is a module to ask for a number without errors
"""


def ask_for_a_number():
    """
    This function does something important
    """

    while True:
        try:
            number = int(input("Give me a number: "))
        except (ValueError, TypeError):
            print("That is not a number")
        else:
            print(f"You entered the number {number}")
            break

    print("Thanks")


ask_for_a_number()
```
