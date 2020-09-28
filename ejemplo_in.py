print("Asignaturas optativas 2020.")
print("Asignaturas: desarrollo web, programación movil, bases de datos distribuidas.")
opcion = input("Escriba la asignatura escogida: ")
asignatura = opcion.lower()
if asignatura in ("desarrollo web","programación movil","bases de datos distribuidas"):
	print("Asignatura disponible.")
	print("Asignatura escogida: " + asignatura)
else:
	print("Asignatura no disponible.")