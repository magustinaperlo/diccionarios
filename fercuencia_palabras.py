palabras = ["hola","como","estas","bien","gracias", "hola"]

frecuencias={}

for palabra in palabras:
    if palabra not in frecuencias:
        frecuencias[palabra] = 1
else:
    frecuencias[palabra] += 1

print(frecuencias)
