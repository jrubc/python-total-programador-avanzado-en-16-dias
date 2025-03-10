## List comprehension

Referst to a concise way to create lists using a specific syntax, allowing for the generation of new lists by applying an expression to each item in an existing iterable, such as a list or range. Example:

```python
pies = [10, 20, 30, 40, 50]
metros = [n / 3.281 for n in pies]
print(metros)

# Commun method
my_list = []
word = "python"
for letter in word:
  my_list.append(letter)

# Comprehension list
my_list = [letter for letter in word]

# Other comprehension lists
my_list = [letter for letter in 'python']
my_list = [n for n in range(0, 21, 2)]
my_list = [n/2 for n in range(0, 21, 2)]
my_list = [n for n in range(0, 21, 2) if n*2 > 10]
my_list = [n if n * 2 > 10 else 'no' for n in range(0, 21, 2)]
```
