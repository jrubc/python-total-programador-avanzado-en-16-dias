# Regular Expresions Module

/d - numeric digit - v\d.\d\d
/w alphanumeric character - \w\w\w-\w\w
/s blank space - number\s\d\d
/D No numeric - \D\D\D\D
/W No alphanumeric - \W\W\W
/S No blank space -\S\S\S\S

```python
import re

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

palabra = "ayuda" in texto
print(palabra)

patron = "ayuda"
busqueda = re.search(patron, texto)
print(busqueda)
if busqueda != None:
    print(busqueda.start())

busqueda = re.findall(patron, texto)
print(busqueda)
if busqueda != None:
    print(busqueda)

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())
```

```python
import re

texto = "llama al 564-525-6588 ya mismo"

patron = r"\d\d\d-\d\d\d-\d\d\d\d"

resultado = re.search(patron, texto)
print(resultado)
if resultado != None:
    print(resultado.group())

print("\n----------------------------------------\n")
patron = r"\d{3}-\d{3}-\d{4}"
resultado = re.search(patron, texto)
print(resultado)
if resultado != None:
    print(resultado.group())

patron = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
resultado = re.search(patron, texto)
print(resultado)
if resultado != None:
    print(resultado.group(2))  # Select a group
```

```python
import re

texto = "No atendemos los martes por la tarde"

buscar = re.search(r"lunes|martes", texto)  # Logic operators

print(buscar)

buscar = re.search(r".demos", texto)  # Logic operators
print(buscar)

buscar = re.search(r"....demos", texto)
print(buscar)

buscar = re.search(r"^\D", texto)  # ^ Check at the begin of the string
print(buscar)

buscar = re.search(r"\D$", texto)  # $ Check at the last of the string
print(buscar)

buscar = re.findall(r"[^\s]", texto)  # [] Exclude
print(buscar)

buscar = re.findall(r"[^\s]+", texto)  # [] Exclude print(buscar)
```
