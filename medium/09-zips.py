# https://docs.python.org/3/library/zipfile.html
import zipfile

# https://stackoverflow.com/questions/7533677/how-to-process-zip-file-with-python/7533721
# Leer los archivos de un zip
with zipfile.ZipFile("path", "r") as z:
    for name in z.namelist():
        data = z.read(name)
        print(name, len(data), repr(data[:10]))
