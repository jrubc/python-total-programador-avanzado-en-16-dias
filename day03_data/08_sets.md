## Sets

Sets are a collection of similar elements to lists but with some differences. Sets can be defined writing the word "sets" and then writing their elements in parentheses and using commas to separate the elements from each other. But this way it is necessary to put the elements in brackets because Python only recognize them as an argument, this is: `sets([1, 2, 3])`
Another way is to write elements in braces like `{1, 2, 3, 4}`
Properties:

- They only accept unique elements (not repeated).
- The elements have no order, meaning they cannot be indexed or sorted.
- They are immutable, so lists or dictionaries cannot be included in them.

```python
my_set = set([1, 2, 3, 4])
my_set = {1, 2, 3, 4}
print(type(my_set))

print(len(my_set))
print(2 in my_set)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

s1.add(4) # Add a item
s1.remove(3) # Remove a item
s1.discard(6) # Discard a element
s1.pop() # Remove a random item
s1.clear() # Clear the set
```
