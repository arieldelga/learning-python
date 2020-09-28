edad = int(input("Por favor introduzca su edad: "))
while edad<=0 or edad>100:
	print("Por favor introduzca una edad real.")
	edad = int(input("Edad: "))
print("<Edad correcta>")