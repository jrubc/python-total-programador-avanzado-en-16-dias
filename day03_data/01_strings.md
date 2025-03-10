# String properties and methods

## Index

Strings in Python have indexes, that is, each character in a string has is its own index that indicates its position in the string.

```
# To know what is the index of a character
my_text = "This is my text"
my_text.index("i") # Search 'i'
my_text.index("i", 4) # Search 'i' since 4 index to the last
my_text.index("i", 4, 10) # Search 'i' since 4 to 9 (10 is not into it)

# To know the character in certain index
my_text[2]
my_text[-2]

# Rindex method
my_text.rindex("i") # Search 'i' since last character to the first (from left to right)
```

## Slicing

Slicing in Python is a technique used to extract a part of a sequence, such as a list, tuple, or string.

```
my_text = "That is my text"
slice = my_text[0:4]
slice = my_text[0:15:2]
print(slice)
```
