lista = []
while True:
    item=input("ingrese un producto a la lista")
    if item=="fin":
        print("cerrar la lista")
        break
    else:
        lista.append(item)
print("los items son:", lista)
eliminar=input("desea remover alguno?")
if eliminar=="si":
    while True:
        item=input("Que producto desea eliminar")
        if item=="fin":
            print("se cierra la lista")
            print("los items de la lista son:", lista)
            break
        else:
            lista.remove(item)
elif eliminar=="no":
    print("los items son", lista)