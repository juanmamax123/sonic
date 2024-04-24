lista=[]
def comenzar():
    print("Bienvenido a tu lista de compras")
    for _ in range(100):
        item=input("ingrese un item: ")
        if item=="fin":
            print("Desea realizar algún cambio?")
            break
        else:
            lista.append(item)

comenzar()

def agregar():
    item=input("Ingrese un item: ")
    lista.append(item)

def editar():
    item=input("¿Qué item quiere editar?: ")
    lista.append(item)

def eliminar():
    item=input("Que Item desea borrar?: ")
    lista.remove(item)

def finalizar():
      item=input("Lista finalizada")
      

while True:
    print("1. Ingresar un nuevo Item, 2. Editar Item, 3. Eliminar Item, 4. Finalizar lista")
    opcion=input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
            agregar()
    elif opcion == '2':
            editar()
    elif opcion == '3':
            eliminar()
    elif opcion == "4":
            finalizar()
            break
    else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
print(lista)

