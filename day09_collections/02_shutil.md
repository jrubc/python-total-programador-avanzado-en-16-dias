# OS and Shutil modules

```python

import os
import shutil

path = "/home/jorgerxbio/downloads/"

for directory, subdirectory, file in os.walk(path):
    print(f"In directory: {directory}")
    print(f"subdirectories: ")
    for sub in subdirectory:
        print(f"{sub}")
    print("Files are: ")
    for f in file:
        print(f"\t{f}")
    print("\n")
```
