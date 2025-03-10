## Loops

Loops are control flow statements that allow you to repeat a given set of operations a number of times. There are two main types of loops:

### For loops

They are generally used to interate over the items in a data collection, such as a list, tuple, string, or dictionary. The basic syntax of a for loop is:

```python
for variable in iterable:
  statements(s)

my_list = ['a', 'b', 'c', 'd']

for letter in my_list:
  number_letter = my_list.index(letter) + 1
  print(f"Letter {number_letter}: {letter}")

for a, b in [[1, 2], [3, 4], [5, 6]]:
  print(a)
  print(b)

dic = {'c1': 'a', 'c2': 'b', 'c3':'c'}

for item in dic:
  print(item)

for item in dic.items:
  print(item)

for item in dic.values:
  print(item)

for a, b in dic.items:
  print(a)
  print(b)
```
