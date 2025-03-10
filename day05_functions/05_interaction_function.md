## Function interaction

```python
from random import shuffle

# Inital list
sticks = ['-', '--', '---', '----']

# Mix sticks
def mix(my_list):
    shuffle(my_list)
    return my_list

# Ask for a number
def try_your_luck():
    attempt = ''

    while attempt not in ['1', '2', '3','4']:
        attempt = input("Choice a number between 1 and 4: ")

    return int(attempt)

# Check attempt
def check_attempt(my_list, attempt):
    if my_list[attempt - 1] == '-':
        print("Let's wash the dishes")
    else:
        print("You are safe this time")

    print(f"You got number {my_list[attempt - 1]}")

mixed_sticks = mix(sticks)
the_choice = try_your_luck()
check_attempt(mixed_sticks, the_choice)
```
