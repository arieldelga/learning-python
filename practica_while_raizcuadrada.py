import math
print("Programa de cálculo de raíz cuadrada.")
num = int(input("Calcular raíz de: "))
intentos = 0
while num<0:
	intentos = intentos+1
	if intentos==4:
		print("<Demasiados intentos, programa finalizado>")
		break;
	print("No se puede hallar la raíz, el número es negativo.")	
	num = int(input("Calcular raíz de:"))

if intentos<4:
	sol = math.sqrt(num)
	print("La raíz de " + str(num) + " es " + str(sol))
