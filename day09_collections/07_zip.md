# Zip module

```python
import zipfile

mi_zip = zipfile.ZipFile("archivo_comprimir.zip", "w")

mi_zip.write("notes.md")

zip_abierto = zipfile.ZipFile("archivo_comprimir.zip", "r")
zip_abierto.extractall()
```
