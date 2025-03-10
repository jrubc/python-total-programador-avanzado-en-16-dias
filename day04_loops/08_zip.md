### Zip

It's a function that mix two or more lists mixing their elements in tuples:

```python
names = ["Ana", "Hugo", "Valeria"]
ages = [65, 29, 42]
cities = ["Lima", "Madrid", "Mexico"]

combined = list(zip(names, ages, cities))
print(combined)

for name, age, city in combined:
    print(f"{name} is {age} and live in {city}")
```
