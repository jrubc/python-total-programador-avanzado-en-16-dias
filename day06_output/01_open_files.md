# Open and modify files

```python
my_file = open("test.txt")
print(my_file)
# print(my_file.read())

print(".: readline :.")
line = my_file.readline()
print(line.rstrip())  # rstrip is for ignore \n

for l in my_file:
    print("Here say: " + l)

print(".: readlines :.")
print(my_file.readlines()) # Print a list with every line

my_file.close()
```
