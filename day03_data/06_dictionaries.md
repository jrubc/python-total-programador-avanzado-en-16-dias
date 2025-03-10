## Dictionaries

Dictionaries are a collection of pairs of elements, these pairs are key-value elements, and each key is unique. How do you write a dictionariy in Python? In braces, the pairs are separated from each other using comma, and key is separated from its value by a colon. Dictionaries have no order.

```python
client = {"nombre": "Juan", "apellido": "Fuentes", "peso": 88, "talla": 1.76}
consult = client["apellido"]  # Get the value of a specify key
print(consult)

# It's possible to nest dictionaries
dictionarie = {"c1": 55, "c2": [10, 20, 30], "c3": {"s1": 100, "s2": 200}}
print(dictionarie["c2"][1])

dictionarie = {"c1": ["a", "b", "c"], "c2": ["d", "e", "f"]}
print(dictionarie["c2"][1].upper())

dictionarie = {1: "a", 2: "b"}
print(dictionarie)

dictionarie[3] = "c"  # Append a item
print(dictionarie)

dictionarie[2] = "B"  # Dictionaries aren't immutable

print(dictionarie.keys())
print(dictionarie.values())
print(dictionarie.items())
```
