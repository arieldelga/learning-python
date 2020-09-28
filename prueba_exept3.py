import math

def calculaRaiz(num1):
	if num1<0:
		raise ValueError("El número no puede ser negativo.")
	else:
		return math.sqrt(num1)

num = int(input("Introduce un número: "))

try:
	print("La raíz es " + str(calculaRaiz(num)))
except ValueError as ErrorDeNumeroImaginario:
	print(ErrorDeNumeroImaginario)

print("<Programa terminado>")