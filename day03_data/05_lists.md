## Lists

Lists are an ordered sequence of elements and can be assigned to a variable and their elements can be of any data type, even a list can be composed of different data types. Lists are written in square brackets and their elements are separated from each other by a comma. They can be nested or indexed, and they also have methods for manipulate them, and aren't immutable.

Definition:

```python
my_list = ['a', 'b', 'c']
```

Index:

```python
my_list[0:3]
```

Concatenation:

```python
my_list2 = ['d', 'e', 'f']
my_list3 = my_list + my_list2
```

Immutable:

```python
my_list3[0] = 'alpha'
```

Methods:

```python
my_list3.append('g')
item_removed = my_list3.pop()
my_list3.sort()
my_list3.reverse()
```
