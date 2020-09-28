valido = False
email = input("Introduzca su email: ")
for i in range(len(email)):
	if email[i] == "@":
		valido = True

if valido:
	print("<El email es correcto>")
else:
	print("<Ele email es incorrecto>")