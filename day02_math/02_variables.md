# Variables

A variable is a named storage location that holds data value, for example, strings, integers, floats, etc.

```
name = "Jorge Oziel"
print(name)
print(type(name))
```

# Rules for variable names

- Redeable: They must be consistent `dog_name = "terry"`
- Unit: They must not have spaces, you can separate words using "\_" like `my_name = "Jorge"`
- Not hispanicisms, for example: instead of año use anio
- You can use numbers, but not at the beginning
- You can't use signs
- You can't use keywords like print, input, string, and that kind of words.

# Casting

Casting is the process of transform one data type to another type. There are two types of casting:

1. Implicit:
   A casting is called implicit when it is Python that converts the data type to another data type automatically, that means, the user doesnot need to do anything. For example:

```
num1 = 20 # This variable is integer
num2 = 30.5 # This variable is a float

num1 = num1 + num2 = # Now num1 is converted automatically toa float
print(num1) # >>> 50.5
print(type(num1)) # >>> <class 'float'>
print(type(num2)) # >>> <class 'float'>
```

2. Explicit:
   A casting is called explicit when it is the user who converts the data type to another. For example:

```
num1 = 5.8
print(num1)
print(type(num1))

num2 = int(num1) # Here's the casting, we conveted a float to an integer
print(num2) # >>>5
print(type(num2)) >>> int <class 'int'>
```
