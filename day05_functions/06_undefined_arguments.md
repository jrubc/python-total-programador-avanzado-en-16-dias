## Undefined arguments

In python, undefined arguments refer to variables that have not been declared or initialized before being used in a function call, or elsewhere in the code. This can lead to errors such as "NameError: name 'variable_name' is not defined" when the interpreter encounters the variable without a prior definition.

When defining a function, if you pass arguments that are not defined, Python will raise an error indicating that the argument is undefined. For example, if you define a function expecting certain arguments but do not provide them or provide them incorrectly, you might receive an error message like "display_results() takes 0 position arguments but 5 were not given" if the function is not set up to accept the given number of arguments.

To hande undefined arguments more elegantly, you can use default values for function parameters, allowring the function to run even if certain arguments are not provided. Adittionally, you can use \*args and \*\*kwargs to accept a variable number of arguments and keyword arguments, respectively.

### Default arguments: By setting default values for function parameters, you can ensure the function can run even if some arguments are not provided. For example:

```python
def my_function(arg1, arg2=None):
    # Function body
```

Here, arg2 has a default value of None, so the function can run even if arg2 is not provided.

### Variable arguments (\*args and \*\*kwargs)

These allow you to pass a variable number of arguments to a function. \*args collects non-keyworded arguments into a tuple, while \*\*kwargs collects keyworded arguments into a dictionary.
Args:

```python
def suma(*args):
    return sum(args)

print(suma(5, 6, 100, 2, 5))
```

Kwargs:

```python
def test(num1, num2, *args, **kwargs):
    print(f"first value is {num1}")
    print(f"second value is {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for key, value in kwargs.intems():
        print(f"{key} = {value}")

args = [100, 200, 300, 400]
kargs = {'x': 'uno', 'y': 'dos'}

test(10, 15, args, kwargs) # This is valid
test(10, 15, 100, 200, 300, 400, x='uno', y='dos') # This is also valid
```
