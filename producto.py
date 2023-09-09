#Diego Alejandro Salamanca
#Crear Menú
menu = {
    1: {"nombre": "Hamburguesa", "precio": 15000},
    2: {"nombre": "Pizza", "precio": 19000},
    3: {"nombre": "Perro", "precio": 8000},
    4: {"nombre": "Papas Fritas", "precio": 5000}
}

#Imprimir Menú
def imprimir_menu():
    print("Menú:")
    for key, value in menu.items():
        print(f"{key}: {value['nombre']} - ${value['precio']}")
        
#Agregar Items al Menú
def agregar_comida():
    nombre = input("Ingrese el nombre de la comida: ")
    precio = float(input("Ingrese el precio de la comida: "))
    nueva_id = max(menu.keys()) + 1
    menu[nueva_id] = {"nombre": nombre, "precio": precio}
    print(f"{nombre} ha sido agregado/a al menú con ID {nueva_id}.")

#Editar Items al Menú
def editar_comida():
    imprimir_menu()
    comida_id = int(input("Ingrese el ID de la comida que desea editar: "))
    if comida_id in menu:
        nombre = input("Ingrese el nuevo nombre de la comida: ")
        precio = float(input("Ingrese el nuevo precio de la comida: "))
        menu[comida_id] = {"nombre": nombre, "precio": precio}
        print(f"Comida con ID {comida_id} editada correctamente.")
    else:
        print("ID de comida no válido.")

#Eliminar Items al Menú
def eliminar_comida():
    imprimir_menu()
    comida_id = int(input("Ingrese el ID de la comida que desea eliminar: "))
    if comida_id in menu:
        del menu[comida_id]
        print(f"Comida con ID {comida_id} eliminada del menú.")
    else:
        print("ID de comida no válido.")

while True:
    print("\nOpciones:")
    print("1. Imprimir menú")
    print("2. Agregar comida")
    print("3. Editar comida")
    print("4. Eliminar comida")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1/2/3/4/5): ")
    
    if opcion == '1':
        imprimir_menu()
    elif opcion == '2':
        agregar_comida()
    elif opcion == '3':
        editar_comida()
    elif opcion == '4':
        eliminar_comida()
    elif opcion == '5':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        
# Diego Alejandro Salamanca



