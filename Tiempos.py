def segundos():
    segundos= int(input("ingrese cantidad de minutos"))
    minutos = segundos / 60
    print (f"{minutos}segundos equivalen a {minutos} minutos. ")
segundos ()

def minutos():
    minutos= int(input("ingrese cantidad de minutos"))
    horas = minutos / 60
    print (f"{horas}segundos equivalen a {horas} horas. ")
minutos ()

def horas():
    horas= int(input("ingrese cantidad de minutos"))
    segundos = horas * 3600
    print (f"{horas}horas equivalen a {segundos} segundos. ")
horas ()
