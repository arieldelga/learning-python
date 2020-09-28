def dividir():
	try:
		num1 = float(input("Introduzca el primer número: "))
		num2 = float(input("Introduzca el segundo número: "))
		print("El resultado es" + str(num1/num2) + ".")
	except ValueError:
		print("Valor incorrecto.")
	except ZeroDivisionError:
		print("No se puede dividir entre cero.")
	finally:
		print("<Cálculo finalizado>")

dividir()