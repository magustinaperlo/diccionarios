"""""
Escribir un programa que cuente la cantidad de veces que aparece una palabra en una oracion que nos ingresa el usuario y 
que al finalizar nos pueda mostrar o que nos devolver lo que contabilizó expresado en un diccionario.
"""""
def contar_palabras(oracion):
    contador = {}
    palabras = oracion.split()
    for palabra in palabras: 
        if palabra in contador:
            contador[palabra]+=1
        else:
            contador[palabra] = 1
    return contador

oracion = input("Ingrese una oración: ")

resultado = contar_palabras(oracion)
print(resultado)
