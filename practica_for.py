arroba = False
punto = False
correo = input("Introduza correo electrónico: ")
for i in correo:
	if (i=="@"):
		arroba=True
		print("hay arroba")
	else:
		if (i=="."):
			punto=True
			print("hay punto")
if (arroba and punto):
	print("El email es correcto.")
else:
	print("El email es incorrecto.")	
