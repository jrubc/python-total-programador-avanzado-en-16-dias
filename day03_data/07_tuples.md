## Tuples

Tuples are collection of elements similar to lists but with one major difference: they are immutable, they are wirtten between parentheses (it is also possible to write them without parentheses) and the elements are separated from each other by commas.
Advantages: They use less memory than lists, and their immutable can be a benefit in avoiding problems with accidental modification of the collection.

```python
my_tuple = (1, 2, 3, 4)
print(my_tuple[2])  # Index is in tuples

my_tuple = list(my_tuple)  # Casting is possible between lists and tuples
print(type(my_tuple))

v, x, y, z = my_tuple  # This assignacion is possible

# Tuples methods
my_tuple = (1, 2, 3, 1)
print(len(my_tuple))
print(my_tuple.count(1))
print(my_tuple.index(1))
```
