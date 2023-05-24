""""
Gestor de Contactos. Crea un programa que funcione como un gestor de contactos. El
programa debe permitir al usuario almacenar nombres y números de teléfono en un
diccionario, así como buscar, agregar y eliminar contactos. Debe mostrar un menú con las
siguientes opciones:
1. Agregar contacto
2. Buscar contacto
3. Eliminar contacto
4. Mostrar todos los contactos
5. Salir
El programa debe ejecutarse hasta que el usuario elija la opción "Salir" del menú.
"""
contactos = {}
bandera = 1
opciones_validas = [1, 2, 3, 4,5]
#cuando opcion sea 5, banedra va a ser 0 
while bandera == 1:
    while True:
        try:
            opcion = int(input("Bienvenidos al gestor de contactos\n1) Agregar contacto \n2) Buscar contacto\n3) Eliminar contacto\n4) Mostrar todos los contactos\n5) Salir\nIngrese una opción: \n"))
            if opcion in opciones_validas:
                break # El usuario ingresó una opción válida, salir del bucle
            else:
                # El usuario ingresó una opción inválida, mostrar mensaje de error y continuar en el bucle
                print("Opción inválida. Intente nuevamente.") # para numeros
        except ValueError:
            # El usuario ingresó algo que no es un número, mostrar mensaje de error y continuar en el bucle
            print("Debe ingresar un número válido. Intente nuevamente.")
    # AGREGAR CONTACTO
    if opcion == 1:
        
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono del contacto: ")
        contactos[nombre] = telefono
        
    #BUSCAR CONTACTO
    if opcion == 2:
        nombre_buscado = input("Ingrese el nombre del contacto que desea buscar: ")
        if nombre_buscado in contactos:
            telefono = contactos[nombre_buscado]
            print("El número de teléfono de", nombre_buscado, "es:", telefono)
        else:
            print("El contacto", nombre_buscado, "no se encuentra en la lista.")
    # ELLIMINAR CONTACTO
    if opcion == 3:
        nombre_buscado = input("Ingrese el nombre del contacto que desea eliminar: ")
        if nombre_buscado in contactos:
            del contactos[nombre_buscado]
            print("Se elimino ", nombre_buscado)
        else:
            print("El contacto", nombre_buscado, "no se encuentra en la lista.")
        
    # MOSTRAR TODOS LOS CONTACTOS
    if opcion == 4:
        for nombre, telefono in contactos.items():
           print("Nombre: " + nombre + ", Telefono: " + telefono)
        
    # SALIR DEL PROGRAMA
    if opcion == 5:
        bandera == 0
        break