# Principles

## Inheritance (Code reusability)

- Inheritance allows a class to inherit attributes and methods from another clas, promoting code reuse.
- Why? Avoid code duplication and makes maintenance easier.

```python
class Animal:
    def __init__(self, age, color):
        self.age = age
        self.color = color

    def be_born(self):
        print("This animal was born")


class Bird(Animal):
    pass


piolin = Bird(2, "yellow")

piolin.be_born()
print(piolin.color)
```

## Extended inheritance

```python
class Animal:
    def __init__(self, age, color):
        self.age = age
        self.color = color

    def be_born(self):
        print("This animal was born")

    def speak(self):
        print("This animal makes a sound")

class Bird(Animal):
    def __init__(self, age, color, flight_height):
        super().__init__(age, color) # Keyword for avoid to write self.astribute...
        self.flight_height = flight_height

    def speak(self): # Overwrite a method of the animal class
        print("pio")

    def fly(self, feets): # Add own method for bird class
        print(f"The bird flies {feets} feets")


piolin = Bird(2, "yellow", 5)

piolin.be_born()
print(piolin.color)
```

## Multiple inheritance

```python
class Father:
    def speak(self):
        print("Hola")

    pass


class Mother:
    def laugh(self):
        print("jasjdfwaerwaf")


class Son(Father, Mother): # Multiple inh
    pass


class Grandson(Son):
    pass


my_grandson = Grandson()

my_grandson.speak()
my_grandson.laugh()
```

## Encapsulation (Data Hiding)

- Encapsulation means building data (attributes) and methods (functions) within a class and restricting direct access to some details.
- Why? It protects internal objects state and enforces controlled access.

## Abstraction (Hiding Complexity)

- Abstraction means hiding complex details and exposing only essential features.
- Why? It simplifies code usage and reduces complexity.

## Polymorphism (Many Forms)

- Polymorphism allows different classes to trated as the same interface, meaning the same method name can have different behaviors.
- Why? It allows flexibility and generalization.
