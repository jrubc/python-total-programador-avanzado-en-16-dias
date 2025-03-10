### While loops

On the other hand these loops repeat as long as a certain boolean condition is met. For example:

```python
count = 0
while count < 5:
  print(count)
  count += 1

  break, continue and pass

coins = 5
while coins > 0:
  print(f"I have {coins} coins")
  coins -= 1
else:
  print("I don't have coins")

while coins > 0:
   pass # Save this site to write code later
else:
  print("I don't have coins")


while coins > 0:
  if coins == 3:
    break # Get out of the loop
else:
  print("I don't have coins")

while coins > 0:
  if coins == 3:
    continue # Break of this iteration but the loop continue with the next iteration
else:
  print("I don't have coins")
```
