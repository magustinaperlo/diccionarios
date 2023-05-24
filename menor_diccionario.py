#Crear una función que solicite al usuario su nombre y su edad de varias personas. Y que devuelva el nombre de la persona más jóven
diccionario = {}
seguir = 0

while True:
    nombre  = input("Ingrese un nombre: ")
    edad = int(input("Ingrese su edad: "))

    diccionario[nombre] = edad

    seguir = int(input("Presione 1 para continuar agregando personas\nPresion 2 para saber quien es mas joven\n"))
    if seguir == 2:
        break

nombre_minimo, edad_minima = min(diccionario.items(), key=lambda x: x[1]) #lambda devuelve la key del value min

print("El más joven es:", nombre_minimo, "y tiene", edad_minima, "años.")

