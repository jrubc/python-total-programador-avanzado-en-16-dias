# Decorators

They are functions that modify the behavior of other functions

```python
"""
Everything in python is a object, inclusive the functions are objects
"""


def upper_case(text):
    print("hello")
    print(text.upper())
    print("goodbye!")


def lower_case(text):
    print(text.lower())


def a_function(function):
    return function


my_function = upper_case  # A function can be assigned to a variable

a_function(upper_case("testing")) # A function can be pass as a argument in a function

my_function("python")
```

```python
"""
Everything in python is a object, inclusive the functions are objects
"""


def change_letters(typ):

    def upper_case(text):
        print("hello")
        print(text.upper())
        print("goodbye!")

    def lower_case(text):
        print(text.lower())

    if typ == "upp":
        return upper_case
    elif typ == "low":
        return lower_case
    else:
        print("Invalid operation type")
        return lambda text: None  # Return a no-op function (does nothing)


my_operation = change_letters("low")

my_operation("word")
```

```python
def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower()):

mayuscula_decorada = decorar_saludo(mayusculas)

mayusculas_decorada('georce')
```

