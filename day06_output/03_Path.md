# Path

```python
import os

path = os.getcwd()  # Get actual directory
path = os.makedirs("/home/jorgerxbio/Repositories/python-courses/other_directory")
path = os.rmdir("/home/jorgerxbio/Repositories/python-courses/other_directory")
path = os.chdir("/home/jorgerxbio/Repositories/python-courses/")

file = open("other_text.txt")
print(file.read())
print(path)

path = "/home/jorgerxbio/Repositories/python-courses/other_text.txt"
element = os.path.basename(path)
print(element)

element = os.path.dirname(path)
print(element)

element = os.path.split(path)
print(element)

# How to create paths for all operating systems
from pathlib import Path

directory = Path("/home/jorgerxbio/Repositories/python-courses/")
file = directory / "other_text.txt"

my_file = open(file)
print(my_file.read())
```
