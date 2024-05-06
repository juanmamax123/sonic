def found_velocidad(distancia,tiempo):
    return distancia / tiempo


def found_distancia(velocidad,tiempo):
    return velocidad*tiempo

def found_tiempo(velocidad,distancia):
    return distancia/velocidad

while True:
    print("1. distancia, 2. velocidad, 3.tiempo")
    opcion=input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        velocidad=float(input("ingrese la velocidad en metros sobre segundos"))
        tiempo=float(input("ingrese su tiempo en segundos"))
    
        found_distancia(velocidad,tiempo)

    elif opcion == '2':
        tiempo=float(input("ingrese la distancia en metros"))
        distancia=float(input("ingrese la distancia en metros"))
        print("resultado ",found_velocidad(distancia,tiempo))
         
    elif opcion == '3':
            velocidad=float(input("ingrese la velocidad en metros sobre segundos"))
            distancia=float(input("ingrese la distancia en metros"))

            found_tiempo(distancia,tiempo)
            break
    else:
            print("Opción no válida. Por favor, seleccione una opción válida.")



