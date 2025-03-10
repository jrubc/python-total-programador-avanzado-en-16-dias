## Random

```python
from random import *

# randint() #Random integer
random = randint(1, 50)
print(random)

# - uniform()
uniform = uniform(1, 5) # Random decimal
uniform = round(uniform(1, 5), 1) # Random number with a decimal
print(uniform)

# - random() # A number between 0 and 1
random = random()

# - choice() # Select a random item into a list
colors = ['blue', 'red', 'green', 'yellow']
choice = choice(colors)
print(choice)

# - shuffle() # Shuffle or mix a list
numbers = list(range(5, 50, 5))
shuffle(numbers)

print(numbers)
)
```
