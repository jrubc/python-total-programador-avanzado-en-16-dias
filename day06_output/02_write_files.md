# Read and write files

```python
file = open("test.txt", "w")
file.write("I am the new text\n")
file.write("Second line hehe\n")
file.write("Third line hehe\n")
file.writelines(["hello", "world", "here", "i", "am"])
file.close()

file = open("test.txt", "a")
file.write("ya llegó tu papi paty")
file.close()

file = open("test.txt", "r")
print(file.read())
file.close()
```
