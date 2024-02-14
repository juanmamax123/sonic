numero_estudiantes = 10
for i in range(1, numero_estudiantes + 1):
  nombre = input(f"Ingrese el nombre del estudiante {i}: \n")
  while True:
    try:
      carne = int(input(f"Ingrese el número de carne del estudiante {i}: \n"))
      if len(str(carne)) == 8:
        break
      else:
        print("\nEl número de carne debe tener 8 dígitos. Ingrese nuevamente: ")
    except ValueError:
      print("\nEl número de carne debe ser un número entero. Ingrese nuevamente: ")
  print(f"\nEstudiante {i}: {nombre}, {carne}\n")
