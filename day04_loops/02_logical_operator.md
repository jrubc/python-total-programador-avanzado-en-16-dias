## Logical operator

Logical operators are symbols or words used to connect two or more expressions to create a compound expression whose value depends only on the original expressions and the meaning of the operator. Common logical operators are AND, OR, and NOT. These operators are fundalmental in programming and are used to create complex boolean expressions that control progam flow and implement decision-making logic.

```python
my_bool = 4 < 5 > 6
print(my_bool)

# And
my_bool = 4 < 5 and 5 > 6

# Or
my_bool = 4 < 5 or 5 > 6

text = "hello python I'm world"
my_bool = ('python' in text) or ('hello' in text)
print(my_bool)

# Not
my_bool = not 4 < 5
my_bool = not (4 < 5)
```
