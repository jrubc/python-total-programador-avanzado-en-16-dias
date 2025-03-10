## Properties

- Immutable

```python
name = "Jorge"
name[0] = 's'
# >>> Error
```

- Concatenable

```python
name = "Jorge"
last = "Rubio"
print(name + " " + last)
# >>> Jorge Rubio
```

- Multiplicable

```python
name = "Jorge"
names= name*5
print(names)
# >>> JorgeJorgeJorgeJorgeJorge
```

- Multiline

```python
name = """Jorge
Rubio"""
print(name)
```

- Check substrings into strings

```python
text = """A thousand small white fish
as if the color of the
wates was boiling
"""
print("thousand" in text)
print("thousand" not in text)
```

- Calculate length

```python
text = """A thousand small white fish
as if the color of the
wates was boiling
"""
print(len(text))
```
