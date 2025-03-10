# Concepts

## Classes

Classes are blueprints, while an object are instances of a class. The instance captures the detailed information about one particular class.

## How to declare a class

```python
class Bird:  # Class declaration
    pass


my_bird = Bird()  # Instance of the Bird class
my_other_bird = Bird()  # Instance of the Bird class

print(my_bird)
print(my_other_bird)
```

## Constructor

A special method to initialize objects.

```python
def __init__(self):
    pass
```

## Methods overloading and overriding

Overloading allows multiple methods with the same name but different parameters, while overriding allows sublass to modify a method from its superclass.

