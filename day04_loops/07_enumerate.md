### Enumerator

This is a function that simplifies the process to access the index of the items in our list.

```python
my_list = ['a', 'b', 'c']
index = 0

for item in my_list:
  print(index, item)
  index += 1

for item in enumerate(my_list):
  print(item)

for index item in enumerate(my_list):
  print(index, item)
```
