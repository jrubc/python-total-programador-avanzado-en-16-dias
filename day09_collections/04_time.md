# Time

```python
import time
import timeit


def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


inicio = time.time()
prueba_for(15000)
final = time.time()

print(f"time: {final-inicio}")

inicio = time.time()
prueba_while(15000)
final = time.time()
print(f"time: {final-inicio}")
```

