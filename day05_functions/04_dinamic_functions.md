## Dinamic functions

```python
def check_3_figures(my_list):
    list_3_figures = []
    for n in my_list:
        if n in range(100, 1000):
            list_3_figures.append(n)
        else:
            pass
    return list_3_figures

result = check_3_figures([553, 992, 5674])
print(result)
```

