dpi=(input("ingrese su dpi: "))
if len(dpi)==13 :
    print("dpi correcto")
    print("el candidato para presidente es partido rojo ")
    print("el candidato para presidente es partido azul ")
    presidente=input("ingrese su voto: ")
    if presidente=="partido rojo":
        print("vote partido rojo")
    elif presidente== "partido azul":
        print ("vote partido azul")
    else:
        print ("voto invalido")
    print(presidente)
    print("el candidato para alcalde es partido rojo")
    print("el candidato para alcalde es partido azul")
    print("el candidato para alcalde es partido verde")
    print("el candidato para alcalde es partido morado")
    alcalde=input("ingrese su voto: ")
    if alcalde=="partido azul":
        print("vote partido azul")
    elif alcalde== "partido rojo":
        print ("vote partido rojo")
    elif alcalde == "partido verde" :
            print ("vote partido verde")
    elif alcalde == "partido morado" :
            print ("vote partido morado")
    else:
        print ("voto invalido")
    print (alcalde)
    guardar=input("quiere guardar su voto: si  no  ")
    if guardar ==("si"):
        print ("sus votos fueron", presidente , alcalde)
    elif guardar ==("no"):
        print("gracias por su voto")
    else:
         print("no respondio")
    print("se logro, nunca va a ganar la une")
else:
    print("dpi incorrecto")