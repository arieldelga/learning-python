print("ACCESO RESTRINGIDO PARA MENORES DE EDAD")
print()
ano_nac = input("Por favor introdizca su año de nacimiento: ")
print()
def esMayor(ano):
	res = False
	if 2019 - ano >= 18:
		res = True
	return res
if esMayor(int(ano_nac)):
	print("ACCESO PERMITIDO")
else:
	print("ACCESO DENEGADO")

print("El programa ha finalizado.")
