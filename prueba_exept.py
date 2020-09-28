def sumar(num1, num2):
	return num1 + num2
def restar(num1, num2):
	return num1 - num2
def multiplicar(num1, num2):
	return num1 * num2
def dividir(num1, num2):
	try:
		return num1/num2
	except ZeroDivisionError:
		print("No se puede dividir entre zero.")
		return "<Operación incorrecta>"

while True:
	try:
		n1 = int(input("Ingrese un número: "))
		n2 = int(input("Ingrese otro número: "))
		break
	except ValueError:
		print("<Valor incorrecto>")
		print("Por favor vuelva a introducir los números.")

op = input("Escriba la operacione que desea realizar (sumar, restar, multiplicar, dividir): ")

if op=="sumar":
	print(sumar(n1, n2))
else:
	if op=="restar":
		print(restar(n1, n2))
	else:
		if op=="multiplicar":
			print(multiplicar(n1, n2))
		else:
			print(dividir(n1, n2))
print("Programa continuando...")			