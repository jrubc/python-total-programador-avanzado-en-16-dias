## Especial methods

```python

class CD:
    def __init__(self, author, title, songs):
        self.author = author
        self.title = title
        self.songs = songs

    def __str__(self):  # Modify the behavior of the special method __str__
        return f"Album: {self.title} by {self.author}"

    def __len__(self):  # Modify the behavior of the special method __len__
        return self.songs

    def __del__(self):
        print("The cd was deleted")


my_cd = CD("Pink Floyd", "The wall", 24)
print(my_cd)
print(len(my_cd))
del my_cd
```
