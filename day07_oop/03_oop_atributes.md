## Atributes

```python
class Bird:  # Class declaration
    pass

    alas = True  # Class atribute

    def __init__(
        self, color
    ):  # Class constructor, it is used to create a instance of this class
        # self parameter represents the instance that will be created
        self.color = color  # Instance atribute


my_bird = Bird("blue")
print(my_bird.color)
```
