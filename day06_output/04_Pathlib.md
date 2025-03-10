# Pathlib

```python
from pathlib import Path, PureWindowsPath

path = Path(
    "/home/jorgerxbio/Repositories/python-courses/programador-avanzado-en-16-dias/test.txt"
)
print(path)
print(path.read_text())
print(path.name)  # File name
print(path.suffix)  # File suffix
print(path.stem)  # File name withour suffix

if not path.exists():
    print("This file don't exists")
else:
    print("This file exists")

# How to transform a path to a Windows path
windows_path = PureWindowsPath(path)
print(windows_path)
   print("This file exists")
```

```python
from pathlib import Path

path = Path(
    "/home/jorgerxbio/Repositories/python-courses/programador-avanzado-en-16-dias/test.txt"
)
guide = Path("Barcelona", "Sagrada_Familia.txt")  # This is a relative path
print(guide)

# How to get the absolute path for a specific site in my sistem?
base = Path.home()
print(base)

guide = Path(
    base, "Europe", "Spain", Path("Barcelona", "Sagrada_Familia.txt")
)  # This is a relative path
print(guide)

guide2 = guide.with_name(("La_Pedrera.txt"))
print(guide2)

print(guide.parent) # Allow us to get the parent of current directory
print(guide.parent.parent)
```

```python
from pathlib import Path

# How to print all txt that are into a directory
guide = Path(Path.home(), "Repositories", "Europa")

for txt in Path(guide).glob("*.txt"):
    print(txt)

print(" .: ----- :. ")
for txt in Path(guide).glob("**/*.txt"):
    print(txt)

guide = Path("Europa", "España", "Sagrada_Familia.txt")
en_europa = guide.relative_to(Path("Europa"))
en_espania = guide.relative_to(Path("Europa", "España"))

print(en_europa)
print(en_espania)
```
