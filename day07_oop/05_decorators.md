## Decorators

Decorators are functions that modify the behavior of other functions or methods. They allow you to wrap another function to add functinality without changing its actual codel

### How decorators work

Decorators use the @decorator_name syntax above a function definition. They take a function as an argument, modify or extend its behavior, and return a new function.

### Built-in Decorators:

1. instance methods: There are regular methods in a class that operate on an instance of the class. They take `self` as their first parameter, which represents the instance.
   - Can access and modify instance attributes
   - Can access other methods
2. @classmethod: Defines a method that receives the class as its first argument.
   ```python
   @classmethod
   def my_method(cls):
       print("something")
   ```
   - They are not associated to the class instances, but to the class itself, so they can be called not only from instances, but also from the class.
   - They can't modify the instance astributes, but can modify class atributes
3. @staticmethod: Defines a static method in a class.
   ```python
   @staticmethod
   def my_method():
       print("something")
   ```
4. @property: Defines a getter method for a class property.
