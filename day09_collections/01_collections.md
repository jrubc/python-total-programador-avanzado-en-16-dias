# Collections Module

```python
from collections import Counter

numbers = [8, 6, 9, 5, 4, 5, 5, 4, 5, 8, 7, 3]
print(Counter(numbers))
print(Counter("Jorge Rubio Miss"))
phrase = "al pan pan y al vino vino"
print(Counter(phrase.split()))

serie = Counter([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3])
print(type(serie))
print(type(serie))
print(serie.most_common())  # Tuples with numbers and their appearances
print(serie.most_common(1))  # Number that most appearances

from collections import defaultdict

mi_dic = {"uno": "verde", "dos": "azul", "tres": "rojo"}
print(mi_dic["dos"])

mi_dic = defaultdict(lambda: "nada")

mi_dic["uno"] = "verde"
print(mi_dic["dos"])

from collections import namedtuple

my_tuple = (500, 18, 65)
print(my_tuple[1])

Person = namedtuple("Person", ["name", "height", "weight"])
ariel = Person("Ariel", 1.76, 79)

print(ariel.height)
```
